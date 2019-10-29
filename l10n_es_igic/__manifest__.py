# -*- encoding: utf-8 -*-
##############################################################################
#
#    Sistemas de Datos, Open Source Management Solution
#    Copyright (C) 2011 Comunitea (https://comunitea.com)
#    Copyright (C) 2014 Arturo Esparragón Goncalves (http://sdatos.com).
#    Copyright (C) 2016-2018 Rodrigo Colombo Vlaeminch (http://sdatos.com).
#    Copyright (C) 2019 Comunitea (https://comunitea.com).
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0
#
##############################################################################

{
    'name': 'IGIC (Impuesto General Indirecto Canario',
    'version': '11.0.1.0.0',
    'author': "David Diz Martínez <daviddiz@gmail.com>,"
              "Atlantux Consultores - Enrique Zanardi,"
              "Sistemas de Datos,"
              "Comunitea,"
              "Factorlibre,"
              "Odoo Community Association (OCA)",
    'category': 'Localisation/Account Charts',
    "website": "https://github.com/OCA/l10n-spain",
    "depends": ['l10n_es'],
    "license": "AGPL-3",
    'data': [
        'data/account_chart_template_igic.xml',
        'data/account_account_common_igic.xml',
        'data/account_tax_group_data.xml',
        'data/taxes_common_igic.xml',
        'data/fiscal_position_common_igic.xml',
        'data/account_chart_template_data.yml'],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
