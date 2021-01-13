# Chronotopic Cartographies - Visualisation Generators, Texts, and Explanatory Guide

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/chronotopic-cartographies/visualisation-generators/HEAD)

This repository contains marked up texts, visualisations, and Python scripts for generating visualisations related to the AHRC-funded *Chronotopic Cartographies for Literature* project at Lancaster University. 

This readme file gives instructions on how to access the tools, either online or on your own computer. Once you're set up, you can get started using the tools by opening the 'start_here.ipynb' notebook.

## Accessing the Tools

### Python Notebooks
The tools for creating the Chronotopic Cartographies maps/graphs are a series of iPython Notebooks (https://jupyter.org/), which are a way for running Python code in a (fairly) user-friendly way. 

There are two ways of running the notebooks. The easiest is to click on the link below, which will open an interactive version of this repository on mybinder.org. This is a good option if you want to try the tools without having to install anything on your own computer. 

https://mybinder.org/v2/gh/chronotopic-cartographies/visualisation-generators/HEAD

Once the binder has loaded, click on the 'start_here.ipynb' notebook, which contains information about the tools and how to start using them.

If you find them useful, you can open them on your own computer using Anaconda, which can be downloaded from here: https://www.anaconda.com/products/individual

Once you've downloaded Anaconda, download this repository and save it to your computer using the link in the toolbar above. Open Anaconda and navigate to the place where you saved this repository then open the 'start_here.inpyb' notebook.

### Gephi
Whichever way you choose to run the iPython notebooks, you will also need to install [Gephi](https://gephi.org/) on your computer. We use Gephi to lay out and edit our graphs before exporting them to create the finished visualisations.

The project contains the following files and folders:

`graphs.ipynb`
The notebook which contains the code for generating graph files from marked-up texts

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

The validator will identify the line at which it realises there is a problem but this is NOT the line where the actual problem is (annoyingly!)   You therefore have to work backwards through the text to identify the problem.  

TROUBLESHOOTING:
All of the troubleshooting relates to inconsistencies which easily slip in!   You have to work through the different elements of coding to find the problem. 

A common problem is when you have marked “topos” at the start of the section but not the end, so it is not closed off.  Go back to the start of the last topos and check if it is OK up to that point then work forwards again. 

The same problem can occur for toporefs – ensure that you have closed the tag.  Work back up from where the problem is identified by Validator until you find an open tag. 

Another really annoying issue is if you have left a space ahead of a toporef name or after it within the XML frame; or used capitals for one name but not for another of the same place.   

A third issue is inconsistent naming of Topoi.  If a place is capitalised in one mention but not in another the computer will read these as different places. E.g. hovel; Hovel. 

You will know once you have corrected all errors because a) you will be at the end of the document and b) the document will validate with a green bar at the bottom stating “valid XML”. 

Once you have finally corrected all errors, save the file, ensuring it has .xml (not .txt) at the end of the file name (alternatively you can delete .txt and insert . xml later).

Place your well-formed XML file in the ‘files/xml/’ folder in the iPython notebook that you cloned earlier.

![XML Folder on Azure](/img/fig-7.png)

Return to the main page.

#### XML Checker

Step 2 checks the valid XML against the Chronotopic Cartographies schema and tells you if there are any issues that still need to be addressed. It makes sure that your sources/targets and connections match up with topoi (without this you end up with duplicate nodes/ floating nodes etc.)

Run the ‘xml_checker.ipynb’ notebook. Edit the input_file_name variable to the name of the XML file you would like to process, then run cells 1 – 4.

![XML checker notebook on Azure](/img/fig-8.png)

After you run the last cell, you’ll get a list of errors and the line numbers they appear on:

![Example errors](/img/fig-9.png)

Correct any errors in the XML file and re-upload the corrected version to ‘files/xml/’.

Note: If you have empty nodes with no attributes, this is generally caused by ‘source’ and ‘target’ attributes in your connection tags being mismatched with the node names – make sure you are consistent.

**Do not proceed until you are sure your XML is valid and all of the attributes in the tags are correct!**

#### Generating the Graph Files using the iPython Notebook

Once you have a clean, valid XML file uploaded to the ‘files/xml/’ folder, go back to the main page of the notebook and run graphs.ipynb.

Click on the first cell of the notebook and then click the ‘run’ button in the toolbar above (this installs all of the libraries needed to generate the graphs).

In the second cell, paste the name of your xml file into the input_file_name variable, between the single quotation marks.

![Input File Name](/img/fig-10.png)

Click run again – an asterisk shows in the square brackets to the left – when this has changed to a number run the next cell.

Run each cell until you reach the end of the notebook. If your XML file was clean and valid, you will now have a series of graph files that you can work with in Gephi.

Come back to the main page of the notebook, navigate to ‘files/graphs’. This now lists all of the graph files you have just generated. The filenames will be based on the input file name you entered earlier, with the extension .gexf rather than .xml.

![.gexf files](/img/fig-11.png)

It’s best to work on the ‘complete’ graph first as this will be the most complex and if you pick up any errors in it here, it will help you with your other maps.

Things to watch out for:

Do your toporefs contain punctuation or spaces at the start or end of the line? These may not show up but will create a problem with validation. 

Is your capitalisation consistent (otherwise the computer will think “Beacon” and “beacon” are two different places)

You can correct errors in individual graphs using Gephi and the data laboratory. This is worth doing if it’s minor errors, but ideally it’s better to fix things in the XML and re-generate the graphs, as otherwise the underlying file will still be wrong. 

In other words, if there are a **lot of errors** go back to the original XML file and correct these first then re-do validation and reload into Python. 


#### Creating and Editing a Graph in GEPHI

Now you are ready to open the downloaded file in Gephi. If you haven’t installed it yet, it can be downloaded for free from here: https://gephi.org/.

Once you’ve installed Gephi, open the graph file created and downloaded in the previous step (file menu at the top of the screen on a Mac).

![A graph file before layout in Gephi](/img/fig-12.png)

The file will look something like this. We can now lay it out for visualisation.

Tip: If you click on the ‘workspace’ menu you can re-name the current workspace in Gephi to the name of the file you are working on – this makes keeping track of your work MUCH easier and means you are not confused about which map you are looking at.

##### Data Laboratory

You can use the ‘data laboratory’ to make final amendments to labels on the graph in Gephi. Gephi automatically opens in ‘overview’. On the top left, you can switch to view the ‘data laboratory’ instead. The data laboratory provides a list of all names on the graph (topoi and toporefs). This means you can eliminate any overlooked minor errors – eg repeated toporefs (eg. “London”; “London.”) and extra spaces after words (eg. “London” “ London ”), or correct typos (Lnodon).

Copy the list from the Data Lab and work through the generated graph following the order in which topoi occur within the text and creating a logical sequential route or series of routes so far as this is possible.

The order of nodes (topoi, toporefs) in the data laboratory thus gives you a normative way of reading. It also provides a means of standardising your graph making. 


##### Graph Layout

First, click on the ‘T’ in the bottom left of the graph window to show the names of your nodes.

Second, use the slider on the right to adjust the size of the font.

Your graph will be unreadable, but don’t panic!

![Graph file with labels](/img/fig-13.png)
![Layout menu - before algorithm selection](/img/fig-14.png)

Gephi comes with a number of algorithms for laying out the graph. We’ve had good results using the ‘Force Atlas 2’ algorithm. Select it from the dropdown menu from layout window on the left bottom.

![Layout menu - after 'force atlas 2' algorithm selection](/img/fig-15.png)

Click the ‘Run’ button to see what happens.

![Graph after layout algorithm has run](/img/fig-16.png)

This is better, but we need to adjust the parameters to get a readable result.

For a complex text, we’ve had good results with the following settings:

Check the ‘dissuade hubs’ and ‘prevent overlap’ checkboxes also bottom left. 

![With 'dissuade hubs' selected](/img/fig-17.png)

With linlog mode also checked the clusters become clearer and more distinct.

You can also experiment with the gravity and scaling attributes.

![With 'lin-log mode ' selected](/img/fig-18.png)

You can also experiment with the gravity and scaling attributes.

Standard scale for a complex novel is 200.
Standard gravity = 15. 
But do play around with the settings depending on your text. 

To recentre the whole map, click on the magnifying glass, found on the righthand edge of the graph screen. Also do this if the map seems to disappear from the screen. To edit a particular section, zoom in and out using two fingers on the mouse pad. 
Remember, you are focusing on readability and visual design. Adjust for clarity (toporefs in particular). 

Note: for complicated texts, you may need to manipulate the basic shape of your map quite drastically, moving a lot of the nodes around. It might be easier to do this without the text showing. You can remove this by unclicking the ‘T’ button. 

If nodes get really spread out also check the stronger gravity box, then reduce the ‘gravity’ to >1. 

Next, on the dropdown menu (as with Force Atlas 2), select and run ‘Label Adjust’ – this will prevent the node text (toporefs) from overlapping.

![Label adjust settings](/img/fig-19.png)

Now, and **only once you have done all the above and are happy with the graph layout**  , you need to adjust the node sizes. Once you’ve adjusted these, you can’t undo the changes. 

You can resize the nodes to emphasise one of two qualities: degree, which is how connected a node is to other nodes in the network; and length, which is the amount of text dedicated to a topos in the underlying XML.

In the top righthand menu (‘Appearance’), click ‘nodes’> the second icon along (to the right of the palette)> ‘ranking’> ‘degree’ (dropdown menu).

![Node scaling settings](/img/fig-20.png)

TIP: for complex texts we recommend having min. size 10, max. size 30. You may have to increase to 10/50.


##### Filtering the *Syuzhet*
To produce the ‘syuzhet’ visualisation of a text, you need to use some of Gephi’s built in functions to ‘filter’ the graph. 

Starting with either the ‘complete’ or ‘topoi’ graph file, from the ‘Filters’ pane (usually on the right hand side of the main window), drag the ‘relation’ item down to the ‘Queries’ pane. Once you have done this, click on it, and edit the ‘pattern’ text box to read ‘direct’.

![Filtering the graph](/img/fig-21.png)

Click on the ‘Filter’ button (with the ‘play’ symbol on it). Your graph will now only show ‘direct’ connections (i.e., spatial connections in the world described by the text). In narratives which describe linear journeys, this frequently corresponds with the syuzhet of the work.

Exporting for Visualisation
Once you are satisfied with your graph layout, go to file>export>graph file (.graphml), and save. **If you have filtered the graph, make sure you click the ‘visible only’ checkbox.**

**NOTE: renaming the ‘Workspace’ is not the same as saving the file so make you enter your new file name at this stage**

#### Final Colour Visualisation

Reopen iPython Notebook. Upload your .graphml file into files/graphs. Copy the name of the graph file to your clipboard.

On the main page, select visualisations and scroll down to the bottom of the page. In the last three cells, paste the graph file name between the single quotes of the input_file_name variable:

![Visualisation file name](/img/fig-22.png)

Scroll back to the top of the page, and run each box in turn, waiting for the asterisks (in square brackets on the left) to change into numbers. **be patient, this can take a few minutes, especially the first cell**

Once you have run the final cell, your colour visualisation should appear at the bottom of the page – looking something like this.

![The final visualisation](/img/fig-22.png)

You can move around it by scrolling with two fingers. Alternatively, you can download it by going to files/svg and downloading it from there. You can then open it using your internet browser. This gives you a better sense of what the whole image looks like – though it is in an un-editable format. This means that you can also compare the visualisation with your Gephi graph, and make changes to the graph accordingly. If there are inconsistencies, you’ll have to go back, change and reimport.

Editing the map in Notebook is quite limited. You need to balance readability of the map (text size) with being able to see the whole image. The things you can change are:

- Size: the size of the output image by changing the 'size' argument (it needs to be a floating point number, so if you want your visualisation twice the size, change it to 2.0).
- Scale: if your visualisation is too small relative to the size of the image, or overflows the boundaries, tweak the 'scale_correction' argument in increments +- 100
- Edge (line) style: change the 'curved' argument to True to add curved connections
- Label position: tweak the position of the labels up and down by adjusting 'label_correction' between 0.1 and 1.0
- Node size: tweak the size of the nodes relative the image using node_scale - int or float values between 0.5 and 5 tend to work okay

**Note:** annoyingly, you can only fully see connection and topoi symbols at this point (Gephi doesn’t display these). This means that, if there’s an error with the code, you’ll have to go back, re-edit in Gephi and reimport.

Once the final visualisation is done, you can download the .svg file from the files/svg folder.

Congratulations you are now a Chronotopic Cartographer!
