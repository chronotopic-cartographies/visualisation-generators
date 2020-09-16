# Chronotopic Cartographies - Visualisation Generators, Texts, and Explanatory Guide

## Literary Topology: An Explanation of the Map Types

Each individual marked-up XML text when processed using a custom Python script generates not one map but a map series.  These present different kinds of spatial relations in the text. We call these graphs “maps” because, although they are topological forms, this is their primary function in relation to a literary text.  They allow for the relative mapping of the internal contents of a text (as opposed to the absolute mapping of the literary world onto the real). We are calling this “literary topology”.  The map types are described below.

### Complete Map
This is a full map of a text showing the topoi (nodes), their associated toporefs (place-names referenced in a node), and the connections between them (lines/arrows). This graph shows the full spatial extent of a text.  The map is helpful for shorter texts (e.g. poems) but becomes overloaded in relation to highly complex texts (e.g. nineteenth-century novels). In such cases it is necessary to show details alongside the master map or to code up and  generate maps for certain sections of the text.  

### Topoi Map
This privileges the topoi (nodes) and the connections between them without displaying their associated toporefs (within a node). Whilst this loses the detail of the complete map, the spatial structure is considerably clearer, and it is therefore useful for visualising longer texts. The map shows place names for nodes but not chronotopic types.

### Topoi and Chronotopic Archetypes
This shows the relationship between the topoi as place-names and their underlying chronotopic types (e.g. “Geneva”/ “Prison”).   Since there is no spatial relationship between the topoi and their underlying chronotopes the connections between them are not coloured.  For many texts this graph therefore appears as disconnected clusters. However, chronotopes become interconnected where the same place name (e.g. “Geneva”) shifts from being identified chronotopically as “Prison” (chronotopic identity 1) to “Idyll” (chronotopic identity 2). Now the clusters become interlinked.  As well as showing the relationship between the chronotopes and the topoi, this therefore also shows how chronotopes can shift dynamically over the course of a text.  Some texts do this far more than others. 

### Deep Chronotope Map
This is the simplest map to understand.  It represents each chronotope as a single node. The size of the nodes reflects the percentage of the text dedicated to each chronotope. This is useful for showing the balance of chronotopic spatio-temporal forms across a text.

### Toporefs and Chronotopic Archetypes
This map shows which toporefs (detailed place names) are associated with a chronotopic archetype (e.g. “road”) showing how a text correlates different places with each spatio-temporal form.

### Syuzhet Map 
This shows the topoi and their connections as they appear sequentially across the text. This is a spatialised visualisation of the “syuzhet” as defined in Proppian narratology: the plot or  narrative as it is told (i.e. may be disordered, fragmented involve flashback etc.). 

### Fabula Map
Partnering with the Syuzhet Map above, the Fabula Map shows the topoi and connections in the order of the story: that is, the order in which events occurred (not necessarily the order as narrated).  This is difficult to achieve for a complex text, so at present fabula maps only exist for shorter poems with the Fabula constructed by re-ordering the Syuzhet rather than generated directly. 

## Guide to Generating Visualisations

### Overview

Generating a Chronotopic Cartographies visualisation is a five step process:

1.  Marking up a text [using the CC XML schema – see separate Guide]
2.  Validating the marked up text
3.  Generating the graph from the XML
4.  Laying out the graph in Gephi
5.  Generating the final visualisation

This document provides instructions for steps 2, 3 and 4.  It assumes that you already have a text marked up using the schema.

### Accessing the Tools
The tools for creating the Chronotopic Cartographies maps/graphs are a series of iPython Notebooks (https://jupyter.org/), which is a tool for running Python code in a (fairly) user-friendly way. Whilst you can run these on your own computer by downloading this repository and installing Jupyter, it’s easier to use Microsoft Azure services, which lets you run iPython notebooks in your web browser without installing any software yourself. If you have a Microsoft account (either through your university or if you have a Hotmail email address or similar), you should have free access to this.

To get started, visit https://notebooks.azure.com/ and sign in using the link in the top right-hand corner.

![Azure Notebooks Sign-in Page](/img/fig-1.png)



