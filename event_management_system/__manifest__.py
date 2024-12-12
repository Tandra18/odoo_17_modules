{
    "name": "Event Management System",
    "website": "togzawyenaung@gmail.com",
    "category": "Productivity",
    "summary": "To manage and control events!",
    "author": "Zaw Ye Naung",
    "application": True,
    "version": "1.0",
    "depends": ['base'],
    "installable": True,
    "data":
    [
        "security/ir.model.access.csv",
        "views/event_views.xml",
        "views/event_form.xml",
        "views/event_views_tree.xml",
        "views/participant_views.xml",
        "views/participant_form.xml",
        "views/participant_views_tree.xml",
        "views/sponsor_views.xml",
        "views/sponsor_form.xml",
        "views/sponsor_views_tree.xml",
        "views/sponsor_agreement_views.xml",
        "views/sponsor_agreement_form.xml",


    ],
    "assests":{
        'web.assets_backend': [
            'event_management_system/static/src/css/style.css',
        ],
    },
}