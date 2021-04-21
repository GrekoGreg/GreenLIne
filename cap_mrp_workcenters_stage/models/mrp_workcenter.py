from odoo import api, fields, models, tools, _


class MrpWorkcenter(models.Model):
    _name = 'mrp.workcenter'
    _inherit = ['mrp.workcenter', 'mail.activity.mixin']

    stage_id = fields.Many2one("mrp.workcenter.stage")
    avg_target = fields.Float("Average Target", compute="_get_avg", store=True)

    def _get_avg(self):
        self = self.search([])
        for rec in self:
            recs = self.env['mrp.workcenter'].search([('stage_id', '=', rec.stage_id.id)])
            rec.avg_target = rec.oee_target / len(recs) if len(recs) > 0 else 1


class MrpWorkcenterStage(models.Model):
    _name = 'mrp.workcenter.stage'

    name = fields.Char("Name")
    sequence = fields.Integer("Sequence")
