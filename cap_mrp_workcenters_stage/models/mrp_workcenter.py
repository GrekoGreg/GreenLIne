from odoo import api, fields, models, tools, _


class MrpWorkcenter(models.Model):
    _name = 'mrp.workcenter'
    _inherit = ['mrp.workcenter', 'mail.activity.mixin']

    stage_id = fields.Many2one("mrp.workcenter.stage")


class MrpWorkcenterStage(models.Model):
    _name = 'mrp.workcenter.stage'

    name = fields.Char("Name")
    sequence = fields.Integer("Sequence")
