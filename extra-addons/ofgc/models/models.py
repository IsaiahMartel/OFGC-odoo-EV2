from odoo import models, fields, api;
# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ofgc(models.Model):
#     _name = 'ofgc.ofgc'
#     _description = 'ofgc.ofgc'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100



class ofgc_schedule(models.Model):
    _name = 'ofgc.schedule'
    _description = 'ofgc.schedule'
    _inherit=['mail.thread','mail.activity.mixin']

    projects = fields.Many2one("ofgc.projects", String="Project", required=True, ondelete="cascade")
    type_schedule = fields.Many2one("ofgc.type_schedule", String="Type-schedule", required=True, ondelete="cascade")
    room = fields.Many2one("ofgc.room", String="Room", required=True, ondelete="cascade")
    date = fields.Date(string="Date")
    hourRange = fields.Char(string="Hour range")
    note = fields.Char(string="Notes")


class ofgc_type_schedule(models.Model):
    _name = 'ofgc.type_schedule'
    _description = 'ofgc.type_schedule'
    _inherit=['mail.thread','mail.activity.mixin']

    schedule = fields.One2many("ofgc.schedule","type_schedule",string="Schedules")
    nameType = fields.Char()
    hourRangeType = fields.Char()

class ofgc_room(models.Model):
    _name = 'ofgc.room'
    _description = 'ofgc.room'
    _inherit=['mail.thread','mail.activity.mixin']

    schedule = fields.One2many("ofgc.schedule","room",string="Schedules")
    nameRoom = fields.Char(string="Name room")
    acronymRoom = fields.Char(string="Acronym room")

class ofgc_projects(models.Model):
    _name = 'ofgc.projects'
    _description = 'ofgc.projects'
    _inherit=['mail.thread','mail.activity.mixin']

    schedule = fields.One2many("ofgc.schedule","projects",string="Schedules")
    seasons = fields.Many2one("ofgc.seasons", String="Season", required=True, ondelete="cascade")
    nameProject = fields.Char()
    startDateProject = fields.Date()
    endDateProject = fields.Date()
    published = fields.Boolean()
    user = fields.Many2one("res.partner",string="Users", required=True, ondelete="cascade")

class ofgc_seasons(models.Model):
    _name = 'ofgc.seasons'
    _description = 'ofgc.seasons'
    _inherit=['mail.thread','mail.activity.mixin']

    projects = fields.One2many("ofgc.projects","seasons",string="Projects")
    nameSeason = fields.Char()
    startDate = fields.Date()
    endDate = fields.Date()
    noteSeason = fields.Char()

class ofgc_users(models.Model):
    _inhertit = 'res.partner'
    projects = fields.One2many("ofgc.projects","user",string="User")


