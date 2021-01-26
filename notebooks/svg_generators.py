import svgwrite
import base64
from lxml import etree
from shapely.geometry import LineString
from shapely.geometry import Point
import math
from geomdl import BSpline
from geomdl import utilities
import numpy as np
from IPython.display import display_svg, SVG
from wand.image import Image


class GraphToSvg():
    """
    Takes a NetworkX graph, returns an SVG
    """
    
    graph = None
        
    def __init__(self, graph):
        self.graph = graph
    
    ## Geometry methods
    
    def calculate_edge_offset(self, line_start, line_end, node_size):
        """Calculate where to start an edge, factoring in the size of the node with which it connects"""
        node_size = int(node_size)
        p = Point(line_end)
        c = p.buffer(node_size + 8).boundary
        l = LineString([(line_start), (line_end)])
        i = c.intersection(l)

        try:
            return i.coords[0]
        except:
            return p.coords[0]


    def angle_between_points(self, a, b):
        """Find the angle between two points on the basis of their coordinates"""
        deltaY = b[1] - a[1]
        deltaX = b[0] - a[0]

        return math.atan2(deltaY, deltaX)


    def calculate_control_points(self, start, end):
        """Calculate the control points for a curved line from the intersection of two circles centered on the start and end points"""

        length = math.sqrt((start[0] - end[0])**2 + (start[1] - end[1])**2)
        p1 = Point(start[0], start[1])
        p2 = Point(end[0], end[1])

        multiplier = 0.6

        c1 = p1.buffer(length * multiplier).boundary
        c2 = p2.buffer(length * multiplier).boundary
        i = c1.intersection(c2)

        if len(i) > 0:
            return (i[0].coords[0], i[1].coords[0])
        else:
            return (start, end)


    def draw_curved_path(self, dwg, start, end, edge_style):
        """Draw a curved path in a given style"""
        start_str = str(start[0]) + ',' + str(start[1])
        end_str = str(end[0]) + ',' + str(end[1])

        case = None

        if edge_style['stroke-case'] > 0:
            if edge_style['stroke-dasharray'] is not None:    
                case = dwg.path(
                    d='M' + start_str,
                    stroke=edge_style['stroke-case-color'],
                    fill='none',
                    stroke_width=edge_style['stroke-case'],
                    stroke_dasharray=edge_style['stroke-dasharray']
                )
            else:
                case = dwg.path(
                    d='M' + start_str,
                    fill='none',
                    stroke=edge_style['stroke-case-color'],
                    stroke_width=edge_style['stroke-case'],
                )


        if edge_style['stroke-dasharray'] is not None:
            path = dwg.path(
                d='M' + start_str, 
                stroke=edge_style['stroke'],
                fill='none',
                stroke_dasharray=edge_style['stroke-dasharray'],
                stroke_width=edge_style['stroke-width']
            )
        else:
            path = dwg.path(
                d='M' + start_str, 
                stroke=edge_style['stroke'],
                fill='none',
                stroke_width=edge_style['stroke-width']
            )

        control_points = self.calculate_control_points(start, end)

        if (start[0] > end[0]):
            control = str(control_points[0][0]) + ', ' + str(control_points[0][1])
        else:
            control = str(control_points[1][0]) + ', ' + str(control_points[1][1])

        path.push('Q' + control + ' ' + end_str)

        if case:
            case.push('Q' + control + ' ' + end_str)
            return path, case
        else:
            return path

    def arrowhead(self, start_x, start_y, end_x, end_y, r):
        """Draw the head of an arrow. Took forever, but adapted the solution from here: https://stackoverflow.com/questions/808826/draw-arrow-on-canvas-tag/36805543#36805543"""
        x_center = end_x
        y_center = end_y

        angle = math.atan2(end_y - start_y, end_x - start_x)
        a = (r * math.cos(angle) + x_center, r * math.sin(angle) + y_center)

        angle += (1/3)*(2*math.pi)
        b = (r * math.cos(angle) + x_center, r * math.sin(angle) + y_center)

        angle += (1/3)*(2*math.pi)
        c = (r * math.cos(angle) + x_center, r * math.sin(angle) + y_center)

        return [a, b, c]
    
    def get_node_size(self, length):
        """
        Returns the size of a node, depending on the 'length' attribute
        """
        if (length < 10):
            return 20
        if (length > 10) and (length < 100):
            return length * 0.3
        if (length > 100) and (length < 1000):
            return length * 0.03
        if (length > 1000):
            return length * 0.003
    
    
    
    def draw_graph(self, output_file, style, size=1.0, scale_correction=700, curved=False, symbology=True, label_correction=1.0, node_scale=5, offset=(0,0)):
        """
        output_file: path to an svg file
        style: a python dictionary defining the styles for nodes and edges
        size: default size is 2000 * 2000 multiplied by the size value
        scale_correction: change this value to alter the size of the graph relative to the total size of the svg canvas
        curved: whether edge connections are curved or not
        symbology: whether or not to use symbology when drawing the graph or a colour scheme
        label_correction: adjusts the position of the labels relative to the centre of the nodes
        node_scale: the size of the nodes relative to canvas
        offset: x y coordinates to offset the centre of the graph - useful when using a background image (as defined in the style)
        """

        dwg_size = (2000 * size, 2000 * size)

        dwg = svgwrite.Drawing(filename=output_file, size=dwg_size, profile='full', debug=True)
        
        rect = dwg.rect(insert=(0,0), size=dwg_size, fill=style['background']['color'])
        
        dwg.add(rect)

        if style['background'].get('image') is not None: 
            path = style['background'].get('image')
            img = Image(filename=path)
            img_data = img.make_blob(format='png')
            encoded = base64.b64encode(img_data).decode()
            png_data = 'data:image/png;base64,{}'.format(encoded)
            image = dwg.add(dwg.image(href=(png_data), insert=(0,0), size=dwg_size, opacity=style['background']['opacity']))
            

        ## Scale the graph to fit the svg canvas

        # First, find the bounds of the graph

        maxX = 0
        maxY = 0
        minX = 0
        minY = 0

        for node in self.graph.nodes():
            data = self.graph.nodes[node] 
            x = data['x']
            y = data['y']
            if (maxX == 0 and maxY == 0 and minX == 0 and minY == 0):
                maxX = x
                maxY = y
                minX = x
                minY = y
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y
            if x < minX:
                minX = x
            if y < minY:
                minY = y

        scale = (max(scale_correction / maxX, scale_correction / maxY)) * size

        # Then calculate the transformation to fit the nodes on the canvas
        
        for node in self.graph.nodes():
            data = self.graph.nodes[node]
            # Translate and scale nodes
            x = float(data['x'])
            y = float(data['y'])
            
            x -= (maxX + minX) / 2
            y -= (maxY + minY) / 2

            x *= scale
            y *= scale

            x += 1050 * size
            y += 1050 * size

            y = (2050 * size) - y 

            # Store translated coordinates, with x,y offset

            self.graph.nodes[node]['x'] = x + offset[0]
            self.graph.nodes[node]['y'] = y + offset[1]

        ## Draw the edges

        edges_group = dwg.add(dwg.g())

        for edge in self.graph.edges():
            data = self.graph.edges[edge]
            # Pull out the sources and targets

            source = edge[0]
            target = edge[1]

            # Find the coordinates of each source and target

            start = (self.graph.nodes[source]['x'], self.graph.nodes[source]['y'])
            end = (self.graph.nodes[target]['x'], self.graph.nodes[target]['y'])
            
            # Shorten the line so it doesn't overlap the symbol

            #source_size = ((float(self.graph.nodes[source]['length']) * 5) / 20) * size
            #target_size = ((float(self.graph.nodes[target]['length']) * 5) / 20) * size
            
            source_size = self.get_node_size(self.graph.nodes[source]['length'])
            target_size = self.get_node_size(self.graph.nodes[target]['length'])
            
            edge_style = None
            
            # First set the edge style to the default of 'None', so if there isn't a connection type a line is still drawn
            for es in style['edges']:
                if es['label'] == None:
                    edge_style = es
            
            # Then go over the connections again and if there is a matching connection type, set that as the edge_style
            for es in style['edges']:
                for v in data.values():
                    if es['label'] == v:
                        edge_style = es
                        break
                    
            if curved == False:
                if edge_style['stroke-case'] > 0:
                    if edge_style['stroke-dasharray'] is None:    
                        edges_group.add(dwg.line(
                            start=start,
                            end=end,
                            stroke=edge_style['stroke-case-color'],
                            stroke_width=edge_style['stroke-case']
                        ))
                    else:
                        edges_group.add(dwg.line(
                            start=start,
                            end=end,
                            stroke=edge_style['stroke-case-color'],
                            stroke_width=edge_style['stroke-case'],
                            stroke_dasharray=edge_style['stroke-dasharray']
                        ))

                if edge_style['stroke-dasharray'] is None:
                    edges_group.add(dwg.line(
                            start=start,
                            end=end,
                            stroke=edge_style['stroke'],
                            stroke_width=edge_style['stroke-width']
                        ))
                else:
                    edges_group.add(dwg.line(
                            start=start,
                            end=end,
                            stroke=edge_style['stroke'],
                            stroke_width=edge_style['stroke-width'],
                            stroke_dasharray=edge_style['stroke-dasharray']
                        ))

                arrowhead_size = 5 * size

                offset = self.calculate_edge_offset(start, end, target_size)

                arrowhead_geom = self.arrowhead(start[0], start[1], offset[0], offset[1], r=arrowhead_size)

                if edge_style['stroke-case'] > 0:
                    fill = edge_style['stroke-case-color']
                else:
                    fill = edge_style['stroke']

                edges_group.add(dwg.polygon(arrowhead_geom, fill=fill))


            else:
                path = self.draw_curved_path(dwg, start, end, edge_style)
                if edge_style['stroke-case'] > 0:
                    edges_group.add(path[1])
                    edges_group.add(path[0])
                else:
                    edges_group.add(path)


                # Calculate arrowhead angle

                angle = self.angle_between_points(start, end)

                control_points = self.calculate_control_points(start, end)

                arrowhead_size = 5 * size

                crv = BSpline.Curve()

                crv.degree = 2

                if (start[0] > end[0]):
                    crv.ctrlpts = [start, control_points[0], end]
                else:
                    crv.ctrlpts = [start, control_points[1], end]

                crv.knotvector = utilities.generate_knot_vector(crv.degree, len(crv.ctrlpts))

                crv.delta = 0.05

                curve_points = crv.evalpts

                l = LineString(curve_points)

                p = Point(end[0], end[1])
                c = p.buffer(target_size).boundary
                i = c.intersection(l)

                arrowhead_geom = None
                
                # If the nodes are too close together, i sometimes returns empty, therefore don't draw the arrowhead
                try:
                    if (start[0] > end[0]):
                        arrowhead_geom = self.arrowhead(control_points[0][0], control_points[0][1], i.coords[0][0], i.coords[0][1], r=arrowhead_size)
                    else:
                        arrowhead_geom = self.arrowhead(control_points[1][0], control_points[1][1], i.coords[0][0], i.coords[0][1], r=arrowhead_size)
                except Exception as e:
                    pass
                    
                    
                if edge_style['stroke-case'] > 0:
                    fill = edge_style['stroke-case-color']
                else:
                    fill = edge_style['stroke']
                
                # If the arrowhead doesn't generate, don't draw it
                
                try:
                    edges_group.add(dwg.polygon(arrowhead_geom, fill=fill))
                except Exception as e:
                    pass
                    


        ## Now draw the nodes

        nodes_group = dwg.add(dwg.g())

        for node in self.graph.nodes():
            data = self.graph.nodes[node]
            x = data['x']
            y = data['y']
            node_size = self.get_node_size(self.graph.nodes[node]['length'])

            circle = nodes_group.add(dwg.circle(stroke='none', fill=style['background']['color'], center=(x,y), r=node_size/2))

            # Get the symbology or colour scheme
            for node_style in style['nodes']:
                for v in data.values():
                    if node_style['label'] == v:
                        with open(node_style['symbol'], 'rb') as file:
                            img = file.read()
                            encoded = base64.b64encode(img).decode()
                            svgdata = 'data:image/svg+xml;base64,{}'.format(encoded)
                            image = nodes_group.add(dwg.image(href=svgdata, insert=(x - (node_size / 2), y - (node_size / 2)), size=(node_size, node_size)))
            
        # Add the labels 
        for node in self.graph.nodes():
            data = self.graph.nodes[node]
            x = data['x']
            y = data['y']
            node_size = self.get_node_size(self.graph.nodes[node]['length']) * size
            font_size = (node_size * label_correction) / 2

            if font_size < 10:
                font_size = 10
            label = nodes_group.add(dwg.text(text=node, insert=(x, y + (node_size * 0.2)), font_size=font_size, text_anchor='middle', font_family=style['label']['font-family'], fill=style['label']['fill']))

        dwg.save()