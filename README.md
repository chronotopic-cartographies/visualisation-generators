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

Once you’ve signed in, you’ll be presented with a screen that looks something like this:

![My Projects Page](/img/fig-2.png)

This is where your projects are stored: if you’ve not used Azure Notebooks before, there won’t be anything here. 

To get started with the tools, you will need to ‘clone’ the project containing the Chronotopic Cartographies tools into your account. This will give you a copy of the tools that you can use (and modify) to generate your own visualisations.

To do this, go to this link: https://notebooks.azure.com/d-hay1/projects/chronocarto-text-proc-vis-gen

![Chronotopic Cartographies Project](/img/fig-3.png)

Click on the ‘Clone’ button, which will bring up this dialogue:

![Clone Project Dialogue](/img/fig-4.png)

Check the ‘I trust the contents of this project’ box, and then click ‘Clone’. The project will then re-open in your workspace. To check that this has indeed occurred,  look at the breadcrumb links at the top of the page. If the project has been cloned successfully into your account, it should look like this:

![Breadcrumbs](/img/fig-5.png)

The project contains the following files and folders:

`graphs.ipynb`
The notebook which contains the code for generating graph files from marked-up texts

`xml_checker.ipynb`
Contains the code for making sure your texts are properly marked-up and tells you where any errors might be.

`visualisations.ipynb`
The code for generating the visualisations from the laid-out Gephi .graphml files

`files/`
Contains the working documents and the outputs from the graph generation and visualisation notebooks. Contains the following sub-folders:

`background_svgs/`
Put background images for ‘referential’ graphs (such as the chessboard for Through the Looking Glass) in this folder

`graphs/`
The graphs generated from your XML files are stored here; upload the .graphml files made with Gephi to this folder.

`svg/`
The final visualisations are saved here

`symbology_colour/`
The icons for the different chronotopes are stored here – you shouldn’t need to touch this unless you want to design your own custom symbology.

`xml/`
Upload your marked-up texts to this folder
 
### Completing the Coding Process
There are two stages to ensuring that the marked-up text is going to successfully generate maps. 

#### Cleaning and Validating the XML
Step 1 is to ensure that your marked-up text is valid XML and can be read by the computer. 

Once all the coding has been done according to the schema, run your XML files through a validator (https://codebeautify.org/xmlvalidator). This will ensure your markup is clean (or ‘well formed’) and will therefore be able to be processed by the graph generation scripts.

Simply copy your entire marked-up text from Sublime Text and paste it into the Validator. Then work through it as the Validator identifies any errors. 

![CodeBeautify XML Validator](/img/fig-6.png)


