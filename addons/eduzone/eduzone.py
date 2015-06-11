from openerp.osv import osv, fields

class event(osv.Model):
    _name = 'event'
    _columns = {
                'name' : fields.char('Name',size=300,required=True),
                'owner' : fields.many2one('res_partner','Owner',domain="[('event_organizer','=',True)]"),
                'type' : fields.selection([('training','Training'),('experiment','Experiment'),
                                           ('meeting','Meeting'),('entertainment','Entertainment'),
                                           ('seminar','Seminar')],'Type',required=True),
                'start_time' : fields.datetime('Start time'),
                'end_time' : fields.datetime('End time'),
                'trainers' : fields.many2many('res_partner',string='Trainers/Speakers',domain="[('is_trainer','=',True)]"),
                'members' : fields.integer('Members'),
                'reserved_resources' : fields.many2many('resource',string='Reserved Resources')                
                }
    
class resource(osv.Model):
    _name = 'resource'
    _columns = {
                'name' : fields.char('Name',size=300,required=True),
                'type' : fields.selection([('device','Device'),('location','Location'),
                                           ('book','Book'),('furniture','Furniture')],
                                          'Type',required=True),
                'reservations' : fields.many2many('reservation',string='Reservations')
                }
    
    
class reservation(osv.Model):
    _name = 'reservation'
    _columns = {
                'resource' : fields.many2one('resource',string='Resource'),
                'event' : fields.many2one('event','Event'),
                'start_time' : fields.datetime('Start time'),
                'end_time' : fields.datetime('End time',)
                }
    
 
    
class res_partner(osv.Model):
    _inherit = 'res.partner'
    _name = 'res_partner'
 
    _columns = {
           'membership_type' : fields.selection([('founder','Founder'),('employee','Employee'),
                                               ('member','Member'),('sponsor','Sponsor'),
                                               ('not_member','Not Member')],'Membership type',required=True),
            'is_trainer' : fields.boolean('Is Trainer'),
            'event_organizer' : fields.boolean('Event Organizer'),
            'skills' : fields.many2many('partner_skill','name',string='Skills')                                          
    }

    
class partner_skill(osv.Model):
    _name = 'partner_skill'
    _columns = {
               'skill_name' : fields.char('Skill',size=20,required=True)
               }
    
    







    