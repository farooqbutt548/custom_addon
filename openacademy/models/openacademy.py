from odoo import fields, models, api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'
    _rec_name = 'name'

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text('Description', help='Add Course description here...')
    # all_detail = fields.One2many('openacademy.session', 'connecting_field', string='All Data')
    responsible_id = fields.Many2one('res.users', string='Responsible', ondelete='set null', index=True)


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Open Academy Session'
    _rec_name = 'name'

    # connecting_field = fields.Many2one('openacademy.course', string="All Details")
    name = fields.Char(string="Name", required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in Days")
    seats = fields.Integer(string="Number of Seats")

    instructor_id = fields.Many2one('res.partner', string='Instructor')
    course_id = fields.Many2one('openacademy.course', string='Course', ondelete='cascade', required=True)
    attendee_id = fields.Many2many('res.partner', string='Attendence')


class BilalFabrics(models.Model):
    _inherit = 'bilal.fabrics'

    email = fields.Char(string="E-Mail")
    zip = fields.Many2one('bilal.products', string="Zip")


class Car(models.Model):
    _name = 'car'

    name = fields.Char('Name')
    price = fields.Float('Price')
    farooq = fields.Char('Farooq butt')

class CarEngin(models.Model):
    _name = 'car.engin'
    _inherits = {'car': 'car_id'}

    car_id = fields.Many2one('car', string="Car")
    name = fields.Char('Car Engin Name')
