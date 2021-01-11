from lxml import etree
import networkx as nx
import pprint
from bs4 import BeautifulSoup, element
import json

class CCXMLValidator:
    """Checks a Chrono-carto encoded XML file for errors"""
    
    xml_element = None
    
    chronotopes = [
        'anti-idyll',
        'castle',
        'distortion',
        'encounter',
        'idyll',
        'metanarrative',
        'parlour',
        'public square',
        'road',
        'threshold',
        'provincial town',
        'wilderness'
    ]

    connections = [
        'direct',
        'indirect',
        'interrupt',
        'jump',
        'charshift',
        'projection',
        'metatextual',
        'paratextual',
        'intratextual',
        'metaphor'
    ]
    
    def __init__(self, file):
        tree = etree.parse(file)
        self.xml_element = tree.getroot()
    
    def check_xml(self):
        """
        Checks for the most common problems with a Chrono-Carto-encoded XML file. 
        WARNING: this doesn't pick up inconsistencies in the naming of topoi, source and target tags
        """

        xml_element = self.xml_element
        chronotopes = self.chronotopes
        connections = self.connections

        errors = {'nodes': [], 'connections': [], 'toporefs': []}

        warnings = {'nodes': [], 'connections': [], 'toporefs': []}

        sources_and_targets = {'sources': [], 'targets': []}

        nodes = []
        
        message = ''

        for topos in xml_element.iter('topos'):
            try:
                topos.attrib['type']
                if topos.attrib['type'] not in chronotopes:
                    warnings['nodes'].append(['Check node type attribute on line ' + str(topos.sourceline), topos.attrib])
            except:
                errors['nodes'].append(['No type attribute on line ' + str(topos.sourceline), topos.attrib])
            try:
                topos.attrib['framename']
                nodes.append(topos.attrib['framename'])
            except:
                errors['nodes'].append(['No framename attribute on line ' + str(topos.sourceline), topos.attrib])


        for connection in xml_element.iter('connection'):
            try:
                connection.attrib['source']
            except:
                errors['connections'].append(['No source attribute on line ' + str(connection.sourceline), connection.attrib])
            try:
                connection.attrib['target']
            except:
                errors['connections'].append(['No target attribute on line ' + str(connection.sourceline), connection.attrib])
            try:
                connection.attrib['relation']
                if connection.attrib['relation'] not in connections:
                    warnings['connections'].append(['Check relation attribute on line ' + str(connection.sourceline), connection.attrib])
            except:
                errors['connections'].append(['No relation attribute on line ' + str(connection.sourceline), connection.attrib])


        for connection in xml_element.iter('connection'):
            try:
                if connection.attrib['source'] not in nodes:
                    sources_and_targets['sources'].append(['No matching topos for source attribute "' + connection.attrib['source'] + '" on line ' + str(connection.sourceline), connection.attrib])
                if connection.attrib['target'] not in nodes:
                    sources_and_targets['targets'].append(['No matching topos for target attribute "' + connection.attrib['target'] + '" on line ' + str(connection.sourceline), connection.attrib])
            except:
                print(connection.sourceline, connection.attrib)


        for toporef in xml_element.iter('toporef'):
            try:
                toporef.attrib['role']
            except:
                errors['toporefs'].append(['No role attribute on line ' + str(toporef.sourceline), toporef.attrib])
            try:
                toporef.attrib['relation']
                if toporef.attrib['relation'] not in connections:
                    warnings['toporefs'].append(['Check relation attribute on line ' + str(toporef.sourceline), toporef.attrib])
            except:
                errors['toporefs'].append(['No relation attribute on line ' + str(toporef.sourceline), toporef.attrib])

        message += 'Errors:\n'
        
        if (len(errors['connections']) > 0) or (len(errors['nodes']) > 0) or (len(errors['toporefs']) > 0):
            message += pprint.pformat(errors)
        else:
            message += 'No errors found!\n'
        
        message += 'Attribute typos:\n'
        
        if (len(warnings['connections']) > 0) or (len(warnings['nodes']) > 0) or (len(warnings['toporefs']) > 0):
            message += pprint.pformat(warnings)
        else:
            message += 'No attribute typos found!\n'

        message += 'Source and Target mis-matches:\n'
        
        if (len(sources_and_targets['sources']) > 0) or (len(sources_and_targets['targets']) > 0):
            message += pprint.pformat(sources_and_targets)
        else:
            message += 'No mismatches found!\n'
        
        print(message)



class GraphGenerator():
    """Base class for all other CC graph generation classes"""
    
    graph = None
    xml_element = None
    xml_dir = None
    output_root = None
    output_dir = None
    output_file = None
    file = None
    
    def __init__(self, xml_dir, output_dir, file):
        tree = etree.parse(xml_dir + file)
        self.xml_element = tree.getroot()
        self.graph = nx.DiGraph()
        self.output_root = file[:-4]
        self.output_dir = output_dir
        self.xml_dir = xml_dir
        self.file = file
    
    def layout(self):
        """Lay out the graph using a spring algorithm"""
        pos = nx.spring_layout(self.graph, center=[0,0])
        
        for node, coords in pos.items():
            self.graph.nodes[node]['x'] = coords[0] * 100
            self.graph.nodes[node]['y'] = coords[1] * 100
    
    def write_gexf(self):
        """Write the graph to gexf"""
        with open(self.output_dir + self.output_file, 'w') as output_file:
            for line in nx.readwrite.gexf.generate_gexf(self.graph):
                output_file.write(line)

    def write_json(self):
        """Write the graph to json"""
        pass
    
    def write_geojson(self):
        """Write the graph to geojson"""
        
        # First, lay out the graph
        self.layout()
        
        geo_dict = {
            'type': 'FeatureCollection',
            'features': []
        }

        for node in self.graph.nodes:
            node_props = self.graph.nodes[node]
            x = node_props['x']    
            y = node_props['y']


            node_props['id'] = node


            node_dict = {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [x, y]
                },
                'properties': node_props
            }
        
        for edge in self.graph.edges:
            edge_props = self.graph.edges[edge]
            source_node = self.graph.nodes[edge[0]]
            target_node = self.graph.nodes[edge[1]]
            source_coords = [source_node['x'], source_node['y']]
            target_coords = [target_node['x'], target_node['y']]

            edge_dict = {
                'type': 'Feature',
                'geometry': {
                    'type': 'LineString',
                    'coordinates': [source_coords, target_coords]
                },
                'properties': edge_props
            }

            geo_dict['features'].append(edge_dict)
    
        geojson = json.dumps(geo_dict, indent = 4)
    
        output_file = self.output_root + '.json'
        
        with open(self.output_dir + output_file, 'w') as file:
            file.write(geojson)
    
        
class CompleteGraphGenerator(GraphGenerator):
    """A complete spatial graph, containing all toporefs and topoi"""
    
    def generate(self):
        self.output_file = self.output_root +'-complete.gexf'
        graph = self.graph
        xml_element = self.xml_element
        
        # Add all the litonyms and topoi as nodes and connections as edges first
        for toporef in xml_element.iter('toporef'):
            graph.add_node('"' + toporef.text + '"', node_type='toporef')

        topos_count = 0

        for topos in xml_element.iter('topos'):
            topos_count_str = str(topos_count)
            try:
                framename = topos.attrib['framename']
                new_length = graph.nodes[framename]['length'] + len(''.join(topos.itertext()).strip())
                graph.nodes[framename]['length'] = new_length
                graph.nodes[framename]['timeframes'] = graph.nodes[framename]['timeframes'] + ',' + topos_count_str

            except KeyError:
                graph.add_node(topos.attrib['framename'], length=len(''.join(topos.itertext()).strip()), chronotope=topos.attrib['type'], node_type="topos", timeframes=topos_count_str)

            topos_count += 1

        for connection in xml_element.iter('connection'):
            try:
                graph.add_edge(connection.attrib['source'], connection.attrib['target'], relation=connection.attrib['relation'])
            except:
                graph.add_edge(connection.attrib['source'], connection.attrib['target'], relation='none')

        # Connect the toporefs to the containing topoi
        for toporef in xml_element.iter('toporef'):
            if ('sequence' in toporef.attrib.keys()):
                pass
            else:
                parent = toporef.getparent()
                containing_node = None
                if parent.tag == 'topos':
                    containing_node = parent.attrib['framename']
                elif parent.tag == 'connection':
                    containing_topos = parent.getparent()
                    try:
                        containing_node = containing_topos.attrib['framename']
                    except:
                        pass
                try:
                    graph.add_edge(containing_node, '"' + toporef.text + '"', relation=toporef.attrib['relation'])
                except:
                    graph.add_edge(containing_node, '"' + toporef.text + '"', relation='none')

        # Connect the toporef sequences to one another
        sequences = {}
        for toporef in xml_element.iter('toporef'):
            try:
                sequence = toporef.attrib['sequence']
                sequences[sequence] = []
            except:
                pass

        for sequence in sequences.keys():
            for toporef in xml_element.iter('toporef'):
                try:
                    sequence = toporef.attrib['sequence']
                    sequences[sequence].append(toporef)
                except:
                    pass

        for sequence, toporef_list in sequences.items():
            prev_toporef = None

            for toporef in toporef_list:    
                if prev_toporef == None:
                    parent = toporef.getparent()
                    containing_node = None
                    if parent.tag == 'topos':
                        containing_node = parent.attrib['framename']
                    elif parent.tag == 'connection':
                        containing_topos = parent.getparent()
                        try:
                            containing_node = containing_topos.attrib['framename']
                        except:
                            pass
                    try:
                        graph.add_edge(containing_node, '"' + toporef.text + '"', relation=toporef.attrib['relation'])
                    except:
                        graph.add_edge(containing_node, '"' + toporef.text + '"', relation='none')

                    prev_toporef = toporef

                else:
                    graph.add_edge('"' + prev_toporef.text + '"', '"' + toporef.text + '"', relation=toporef.attrib['relation'])
                    prev_toporef = toporef

                    
class SyuzhetGraphGenerator(GraphGenerator):
    def generate(self):
        """
        Takes an XML element marked up using the CC schema and returns a populated graph of the spatial nodes, connected sequentially as they appear in the text. Corresponds (loosely) with the syuzhet or story order of the text.
        """

        self.output_file = self.output_root +'-syuzhet.gexf'
        graph = self.graph
        xml_element = self.xml_element
        
        topoi = []

        for topos in xml_element.iter('topos'):
            topoi.append([topos.attrib['framename'], topos.attrib['type'], len(''.join(topos.itertext()).strip())])

        prev_node = None

        for t in topoi:
            if prev_node == None:
                prev_node = t[0]
                graph.add_node(t[0], chronotope=t[1], length=t[2])
            else:
                try:
                    graph.nodes[t[0]]['length'] += t[2]
                except KeyError:
                    graph.add_node(t[0], chronotope=t[1], length=t[2])

                connection = None

                for c in xml_element.iter('connection'):
                    if (c.attrib['source'] == prev_node) and (c.attrib['target'] == t[0]):
                        graph.add_edge(prev_node, t[0], relation=c.attrib['relation'])
                        connection = [prev_node, t[0], c.attrib['relation']]
                    else:
                        #graph.add_edge(prev_node, t[0], relation='none')
                        connection = [prev_node, t[0], 'none']

                prev_node = t[0]


class TopoiGraphGenerator(GraphGenerator):
    def generate(self):
        """
        Iterate over an XML element and its children and generate a graph of topoi nodes and connections, including attributes.
        """
        
        self.output_file = self.output_root +'-topoi.gexf'
        graph = self.graph
        xml_element = self.xml_element
        
        for topos in xml_element.iter('topos'):
            try:
                graph.nodes[topos.attrib['framename']]['length'] += len(''.join(topos.itertext()).strip())
            except KeyError:
                graph.add_node(topos.attrib['framename'], chronotope=topos.attrib['type'], length=len(''.join(topos.itertext()).strip()))

        for c in xml_element.iter('connection'):
            try:
                graph.add_edge(c.attrib['source'], c.attrib['target'], relation=c.attrib['relation'])
            except KeyError:
                pass

            
class TemporalTopoiGraphGenerator(GraphGenerator):
    def generate(self):
        """
        Takes an XML element and sequentially builds a populated graph of topoi, recording the temporal index, size, and chronotope 
        of each as they are encountered, and the temporal index of the connecting edges.
        """
        
        self.output_file = self.output_root +'-temporal-topoi.gexf'
        graph = self.graph
        xml_element = self.xml_element
        
        topoi = {}
        connections = []
        index = 0

        for el in xml_element.iter():
            if el.tag == 'topos':
                if el.attrib['framename'] not in topoi.keys():
                    topoi[el.attrib['framename']] = {}
                    topoi[el.attrib['framename']]['chronotopes'] = [el.attrib['type']]
                    topoi[el.attrib['framename']]['timeframes'] = [str(index)]
                    topoi[el.attrib['framename']]['text_lengths'] = [str(len(el.text))]
                else:
                    topoi[el.attrib['framename']]['chronotopes'].append(el.attrib['type'])
                    topoi[el.attrib['framename']]['timeframes'].append(str(index))
                    topoi[el.attrib['framename']]['text_lengths'].append(str(len(el.text)))



            if el.tag == 'connection':
                connection = {}
                connection['source'] = el.attrib['source']
                connection['target'] = el.attrib['target']
                connection['relation'] = el.attrib['relation']
                connection['source_index'] = index 
                connection['target_index'] = index +1
                connections.append(connection)

                index = index +1

        for node, attributes in topoi.items():
            chronotopes = ', '.join(attributes['chronotopes'])
            indices = ', '.join(attributes['timeframes'])
            text_lengths = ', '.join(attributes['text_lengths'])
            graph.add_node(node, chronotopes=chronotopes, time_indices=indices, text_lengths=text_lengths)

        for edge in connections:
            graph.add_edge(edge['source'], edge['target'], source_index=edge['source_index'], target_index=edge['target_index'], relation=edge['relation'])
        

    def generate_simple(self):
        """
        Takes an XML element and builds a graph of topoi, recording only timeframes
        """
        self.output_file = self.output_root +'-temporal-topoi-simple.gexf'
        graph = self.graph
        xml_element = self.xml_element
        
        graph.clear()
        
        topos_count = 0
    
        for topos in xml_element.iter('topos'):
            topos_count_string = str(topos_count)
            try:
                graph.nodes[topos.attrib['framename']]['length'] += len(''.join(topos.itertext()).strip())
                timeframes = graph.nodes[topos.attrib['framename']]['timeframes'] + ',' + topos_count_string 
                graph.nodes[topos.attrib['framename']]['timeframes'] = timeframes
            except KeyError:
                graph.add_node(topos.attrib['framename'], chronotope=topos.attrib['type'], length=len(''.join(topos.itertext()).strip()), timeframes=topos_count_string)

            topos_count += 1


        for c in xml_element.iter('connection'):
            try:
                graph.add_edge(c.attrib['source'], c.attrib['target'], relation=c.attrib['relation'])
            except KeyError:
                pass

class TopoiAndArchetypeGraphGenerator(GraphGenerator):
    def generate(self):
        """
        Takes an XML element marked up using CLAYE and returns a populated graph of the topoi and their associated chronotopes
        """
        
        self.output_file = self.output_root + '-topoi-and-chronotopic-archetypes.gexf'
        graph = self.graph
        xml_element = self.xml_element
        
        for topos in xml_element.iter('topos'):
            graph.add_node(topos.attrib['type'], node_type='chronotope')
            graph.add_node(topos.attrib['framename'], node_type='setting')
            graph.add_edge(topos.attrib['type'], topos.attrib['framename'])


class DeepChronotopesGraphGenerator(GraphGenerator):
    def generate(self):
        """
        Creates a 'deep' chronotopes map, ie. the distribution of chronotopes across a text, and how they are connected with one another. Uses Beautifulsoup instead of eTree because XML is a nightmare.
        """
        
        with open(self.xml_dir + self.file) as fp:
            soup = BeautifulSoup(fp, features="lxml")
        
        self.output_file = self.output_root +'-deep-chronotopes.gexf'
        graph = self.graph
        
        # Add all the connections first
        edges = []
        for connection in soup.find_all('connection'):
            source = connection.get('source')
            target = connection.get('target')
            relation = connection.get('relation')

            source_chronotope = None
            target_chronotope = None

            if (connection.parent.get('framename') == source):
                source_chronotope = connection.parent.get('type')

            else:
                for el in connection.previous_elements:
                    if (isinstance(el, element.Tag) == True):
                        if el.get('framename') == source and source_chronotope is None:
                            source_chronotope = el.get('type')
                        elif el.get('framename') == target and target_chronotope is None:
                            target_chronotope = el.get('type')

            for el in connection.next_elements:
                if (isinstance(el, element.Tag) == True and el.get('type') is not None):
                    if el.get('framename') == target and target_chronotope is None:
                        target_chronotope = el.get('type')
                    elif el.get('framename') == source and source_chronotope is None:
                        source_chronotope = el.get('type')

            if (source_chronotope != None and target_chronotope != None):
                edges.append((source_chronotope, target_chronotope, relation))

        edges = list(set(edges))

        for e in edges:
            graph.add_edge(e[0], e[1], relation=e[2])

        # Then iterate over the topoi and calculate the number of characters in each, appending the values to the nodes
        chronotopes = {}
        for topos in soup.find_all('topos'):
            chronotope = topos.get('type')
            try:
                if chronotope not in chronotopes.keys():
                    chronotopes[chronotope] = len(topos.get_text())
                else:
                    chronotopes[chronotope] += len(topos.get_text())
            except:
                pass

        for c, attribs in chronotopes.items():
            graph.nodes[c]['length'] = attribs  


class ArchetypesAndToporefsGraphGenerator(GraphGenerator):
    def generate(self):
        """
        Takes an XML element marked up using the CC schema and returns a populated graph of the chronotope archteypes, 
        their connections, and their associated toporefs.
        """
        
        self.output_file = self.output_root + '-topoi-and-chronotopic-archetypes.gexf'
        graph = self.graph
        xml_element = self.xml_element
        
        topoi = {}
        for topos in xml_element.iter('topos'):
            try: 
                chronotope = topos.attrib['type']
                graph.nodes[chronotope]['length'] += len(''.join(topos.itertext()).strip())
            except KeyError:
                graph.add_node(topos.attrib['type'], length=len(''.join(topos.itertext()).strip()))
            topoi[topos.attrib['framename']] = topos.attrib['type']

        for connection in xml_element.iter('connection'):
            try:
                source_chronotope = topoi[connection.attrib['source']]
                target_chronotope = topoi[connection.attrib['target']]
                relation = connection.attrib['relation']
                graph.add_edge(source_chronotope, target_chronotope, relation=relation)
            except:
                pass

        for topos in xml_element.iter('topos'):
            try:
                chronotope = topos.attrib['type']
                for toporef in topos.iter('toporef'):
                    graph.add_edge(chronotope, '"' + toporef.text + '"', relation=toporef.attrib['relation'])
            except:
                pass
            

def generate_all(xml_dir, output_dir, input_file):
    """
    Generate ALL the graphs
    """
    # Complete
    complete = CompleteGraphGenerator(xml_dir=xml_dir, output_dir=output_dir, file=input_file)
    complete.generate()
    complete.write_gexf()
    
    # Syuzhet
    syuzhet = SyuzhetGraphGenerator(xml_dir=xml_dir, output_dir=output_dir, file=input_file)
    syuzhet.generate()
    syuzhet.write_gexf()
    
    # Topoi
    topoi = TopoiGraphGenerator(xml_dir=xml_dir, output_dir=output_dir, file=input_file)
    topoi.generate()
    topoi.write_gexf()
    
    # Time Topoi
    time_topoi = TemporalTopoiGraphGenerator(xml_dir=xml_dir, output_dir=output_dir, file=input_file)
    time_topoi.generate()
    time_topoi.write_gexf()
    time_topoi.generate_simple()
    time_topoi.write_gexf()
    
    # Topoi and Archetypes
    topoi_and_archetypes = TopoiAndArchetypeGraphGenerator(xml_dir=xml_dir, output_dir=output_dir, file=input_file)
    topoi_and_archetypes.generate()
    topoi_and_archetypes.write_gexf()
    
    # Deep Chronotopes
    deep_chronotopes = DeepChronotopesGraphGenerator(xml_dir=xml_dir, output_dir=output_dir, file=input_file)
    deep_chronotopes.generate()
    deep_chronotopes.write_gexf()
    
    toporefs_and_archetypes = ArchetypesAndToporefsGraphGenerator(xml_dir=xml_dir, output_dir=output_dir, file=input_file)
    toporefs_and_archetypes.generate()
    toporefs_and_archetypes.write_gexf()