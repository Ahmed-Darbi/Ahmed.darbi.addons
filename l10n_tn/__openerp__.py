# -*- encoding: utf-8 -*-

{
    "name" : "Comptabilité - Tunisienne",
    "version" : "1.0",
    "author" : "Darbi Ahmed",
    "website": "",
    "category" : "Localization/Account Charts",
    "description": """
Ceci est le module de base pour gérer la comptabilité pour la Tunisie .
=================================================================

Ceci est le module de base pour gérer la comptabilité pour la Tunisie""",

    "depends" : ['base','account'],
    "init_xml" : [],
    "data" : [
        'plan_comptable_general.xml',
        'tn_pcg_taxes.xml',
        'tn_tax.xml',
		'l10n_tn_wizard.xml',
        'security/ir.model.access.csv',
		     ],
    "test": [],
    "demo_xml" : [],
    "active": True,
    "installable": True,
	'images': ['images/config_chart_l10n_tn.jpg', 'images/l10n_tn_chart.jpg'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
