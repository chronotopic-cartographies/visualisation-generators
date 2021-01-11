colour_style = {
    'title': {
        'font-family': "'Baskerville', serif",
        'fill': '#dbdbdb',
        'size': 64
    },
    'border': { 
        'stroke-width': 2,
        'stroke': 'white'
    },
    'legend': {
        'font-family': "'Helvetica Neue', sans-serif",
        'fill': '#dbdbdb',
        'size': 24
    },
    'legend_heading': {
        'font-family': "'Baskerville', serif",
        'fill': '#dbdbdb',
        'size': 42
    },
    'label': {
        'font-family': "'Helvetica Neue', sans-serif",
        'fill': '#dbdbdb',
        'size': 0.6
    },
    'background': {
        'color': '#525252',
        # To add a background image, uncomment the lines below and change the name of the file
        'image': 'files/background_svgs/swallows_and_amazons.png',
        'opacity': 0.6
    },
    'edges': [
        {
            'label': 'direct',
            'stroke': '#525252', 
            'stroke-width': 1, 
            'stroke-dasharray': None, 
            'stroke-linecap': 'round',
            'stroke-case': 3,
            'stroke-case-color': '#c686e9'
        },
        {
            'label': 'indirect',
            'stroke': '#525252', 
            'stroke-width': 1, 
            'stroke-dasharray': '6,6', 
            'stroke-linecap': 'round',
            'stroke-case': 3,
            'stroke-case-color': '#c686e9'
        },
        {
            'label': 'interrupt',
            'stroke': '#ff7f33', 
            'stroke-width': 2, 
            'stroke-dasharray': '20,10', 
            'stroke-linecap': 'round',
            'stroke-case': 0,
            'stroke-case-color': '#ff7f33'
        },
        {
            'label': 'jump',
            'stroke': '#ff7f33', 
            'stroke-width': 2, 
            'stroke-dasharray': '40,10', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#ff7f33'
        },
        {
            'label': 'charshift',
            'stroke': '#00caff', 
            'stroke-width': 2, 
            'stroke-dasharray': '40,10', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#00caff'
        },
        {
            'label': 'metaphor',
            'stroke': '#00caff', 
            'stroke-width': 2, 
            'stroke-dasharray': '20,5', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#00caff'
        },
        {
            'label': 'projection',
            'stroke': '#ff7f33', 
            'stroke-width': 2, 
            'stroke-dasharray': '10,40', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#ff7f33'
        },
        {
            'label': 'metatextual',
            'stroke': '#5fc613', 
            'stroke-width': 2, 
            'stroke-dasharray': '2,8', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#5fc613'
        },
        {
            'label': 'paratextual',
            'stroke': '#5fc613', 
            'stroke-width': 2, 
            'stroke-dasharray': '2,20', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#5fc613'
        },
        {
            'label': 'intratextual',
            'stroke': '#5fc613', 
            'stroke-width': 2, 
            'stroke-dasharray': '2,5,2,30', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#5fc613'
        },
        {
            'label': 'none',
            'stroke': '#c1c1c1', 
            'stroke-width': 2, 
            'stroke-dasharray': '2,8', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#c1c1c1'
        },
        {
            'label': None,
            'stroke': '#c1c1c1', 
            'stroke-width': 2, 
            'stroke-dasharray': '2,8', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#c1c1c1'
        }
    ],
    'nodes': [
        {
            'label': 'anti-idyll',
            'color': '#ddfdea', 
            'symbol': 'files/symbology_colour/anti_idyll.svg'
        },
        {   
            'label': 'castle',
            'color': '#8df8b7', 
            'symbol': 'files/symbology_colour/castle.svg'
        },
        {
            'label': 'distortion',
            'color': '#4df48f', 
            'symbol': 'files/symbology_colour/distortion.svg'
        },
        {
            'label': 'encounter',
            'color': '#9df9c1', 
            'symbol': 'files/symbology_colour/encounter.svg'
        },
        {
            'label': 'idyll',
            'color': '#cdfcdf', 
            'symbol': 'files/symbology_colour/idyll.svg'
        },
        {
            'label': 'metanarrative',
            'color': '#3df384', 
            'symbol': 'files/symbology_colour/metalepsis.svg'
        },
        {
            'label': 'parlour',
            'color': '#5df599', 
            'symbol': 'files/symbology_colour/parlour.svg'
        },
        {
            'label': 'public square',
            'color': '#6df6a3', 
            'symbol': 'files/symbology_colour/public_square.svg'
        },
        {
            'label': 'road',
            'color': '#bdfbd5', 
            'symbol': 'files/symbology_colour/road.svg'
        },
        {
            'label': 'threshold',
            'color': '#adfacb', 
            'symbol': 'files/symbology_colour/threshold.svg'
        },
        {
            'label': 'provincial town',
            'color': '#7df7ad', 
            'symbol': 'files/symbology_colour/town.svg'
        },
        {
            'label': 'wilderness',
            'color': '#edfef4', 
            'symbol': 'files/symbology_colour/wilderness.svg'
        }
    ]
}


print_style = {
    'title': {
        'font-family': "'Baskerville', serif",
        'fill': '#3c3c3b',
        'size': 64
    },
    'border': { 
        'stroke-width': 2,
        'stroke': 'white'
    },
    'legend': {
        'font-family': "'Helvetica Neue', sans-serif",
        'fill': '#3c3c3b',
        'size': 24
    },
    'legend_heading': {
        'font-family': "'Baskerville', serif",
        'fill': '#3c3c3b',
        'size': 42
    },
    'label': {
        'font-family': "'Helvetica Neue', sans-serif",
        'fill': '#3c3c3b',
        'size': 0.6
    },
    'background': {
        'color': '#ffffff',
        # To add a background image, uncomment the lines below and change the name of the file
        #'image': 'files/background_svgs/swallows_and_amazons.png',
        #'opacity': 0.4
    },
    'edges': [
        {
            'label': 'direct',
            'stroke': '#ffffff', 
            'stroke-width': 1, 
            'stroke-dasharray': None, 
            'stroke-linecap': 'round',
            'stroke-case': 3,
            'stroke-case-color': '#000000'
        },
        {
            'label': 'indirect',
            'stroke': '#ffffff', 
            'stroke-width': 1, 
            'stroke-dasharray': '6,6', 
            'stroke-linecap': 'round',
            'stroke-case': 3,
            'stroke-case-color': '#000000'
        },
        {
            'label': 'interrupt',
            'stroke': '#000000', 
            'stroke-width': 2, 
            'stroke-dasharray': '20,10', 
            'stroke-linecap': 'round',
            'stroke-case': 0,
            'stroke-case-color': '#ff7f33'
        },
        {
            'label': 'jump',
            'stroke': '#000000', 
            'stroke-width': 2, 
            'stroke-dasharray': '40,10', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#ff7f33'
        },
        {
            'label': 'charshift',
            'stroke': '#000000', 
            'stroke-width': 2, 
            'stroke-dasharray': '40,10', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#00caff'
        },
        {
            'label': 'metaphor',
            'stroke': '#000000', 
            'stroke-width': 2, 
            'stroke-dasharray': '20,5', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#00caff'
        },
        {
            'label': 'projection',
            'stroke': '#000000', 
            'stroke-width': 2, 
            'stroke-dasharray': '10,40', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#ff7f33'
        },
        {
            'label': 'metatextual',
            'stroke': '#000000', 
            'stroke-width': 2, 
            'stroke-dasharray': '2,8', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#5fc613'
        },
        {
            'label': 'paratextual',
            'stroke': '#000000', 
            'stroke-width': 2, 
            'stroke-dasharray': '2,20', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#5fc613'
        },
        {
            'label': 'intratextual',
            'stroke': '#000000', 
            'stroke-width': 2, 
            'stroke-dasharray': '2,5,2,30', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#5fc613'
        },
        {
            'label': 'none',
            'stroke': '#575756', 
            'stroke-width': 2, 
            'stroke-dasharray': '2,8', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#575756'
        },
        {
            'label': None,
            'stroke': '#575756', 
            'stroke-width': 4, 
            'stroke-dasharray': '4,8', 
            'stroke-linecap': 'square',
            'stroke-case': 0,
            'stroke-case-color': '#575756'
        }
    ],
    'nodes': [
        {
            'label': 'anti-idyll',
            'color': '#ddfdea', 
            'symbol': 'files/symbology_greyscale/anti_idyll.svg'
        },
        {   
            'label': 'castle',
            'color': '#8df8b7', 
            'symbol': 'files/symbology_greyscale/castle.svg'
        },
        {
            'label': 'distortion',
            'color': '#4df48f', 
            'symbol': 'files/symbology_greyscale/distortion.svg'
        },
        {
            'label': 'encounter',
            'color': '#9df9c1', 
            'symbol': 'files/symbology_greyscale/encounter.svg'
        },
        {
            'label': 'idyll',
            'color': '#cdfcdf', 
            'symbol': 'files/symbology_greyscale/idyll.svg'
        },
        {
            'label': 'metanarrative',
            'color': '#3df384', 
            'symbol': 'files/symbology_greyscale/metalepsis.svg'
        },
        {
            'label': 'parlour',
            'color': '#5df599', 
            'symbol': 'files/symbology_greyscale/parlour.svg'
        },
        {
            'label': 'public square',
            'color': '#6df6a3', 
            'symbol': 'files/symbology_greyscale/public_square.svg'
        },
        {
            'label': 'road',
            'color': '#bdfbd5', 
            'symbol': 'files/symbology_greyscale/road.svg'
        },
        {
            'label': 'threshold',
            'color': '#adfacb', 
            'symbol': 'files/symbology_greyscale/threshold.svg'
        },
        {
            'label': 'provincial town',
            'color': '#7df7ad', 
            'symbol': 'files/symbology_greyscale/town.svg'
        },
        {
            'label': 'wilderness',
            'color': '#edfef4', 
            'symbol': 'files/symbology_greyscale/wilderness.svg'
        }
    ]
}