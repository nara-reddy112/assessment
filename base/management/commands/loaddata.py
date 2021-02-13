import os
import xlrd
from django.core.management.base import BaseCommand, CommandError
from base.models import User,Activities 

class Command(BaseCommand):
	help = 'Load data to database'

	def add_arguments(self, parser):
		parser.add_argument('path', nargs='+', type=str)

	def handle(self, *args, **options):
		path = options['path']
		isFile = os.path.isfile(path[0])
		if isFile:
			self.stdout.write(self.style.SUCCESS("PATH found"))
			wb = xlrd.open_workbook(path[0])
			sheet = wb.sheet_by_index(0)
			sheet.cell_value(0, 0)
			for i in range(1,sheet.nrows):
				# import pdb;pdb.set_trace()
				user_data = sheet.row_values(i)[0:3]
				usr_inst = User.objects.create(id=user_data[0],real_name=user_data[1],tz=user_data[2])
				self.stdout.write(self.style.SUCCESS(user_data[1]))
				activity_data = sheet.row_values(i)[3:sheet.ncols]
				for act in range(0,len(activity_data),2):
					self.stdout.write(self.style.SUCCESS(activity_data[act]))
					Activities.objects.create(user=usr_inst,start_time=activity_data[act],end_time=activity_data[act+1])
					self.stdout.write(self.style.SUCCESS(activity_data[act+1]))
					# Activities.objects.create(user=usr_inst,end_time=activity_data[act+1])

				# for user in user_data:
				# 	self.stdout.write(self.style.SUCCESS((user[1])))
				# 	# usr_inst = User.objects.create(id=user[0],real_name=user[1],tz=user[2])
				# 	for act in range(0,len(activity_data),2):
				# 		self.stdout.write(self.style.SUCCESS(activity_data[act]))
				# 		self.stdout.write(self.style.SUCCESS(activity_data[act+1]))
				# 		# Activities.objects.create(user=usr_inst,)
				# self.stdout.write(self.style.SUCCESS(sheet.row_values(i)))
				# for j in range(sheet.ncols):
				# 	self.stdout.write(self.style.SUCCESS((sheet.cell_value(i, j))))
			pass
		else:
			self.stdout.write(self.style.SUCCESS("PATH not found")) 
		# for poll_id in options['poll_ids']:
		# 	try:
		# 		poll = Poll.objects.get(pk=poll_id)
		# 	except Poll.DoesNotExist:
		# 		raise CommandError('Poll "%s" does not exist' % poll_id)

		# 	poll.opened = False
		# 	poll.save()

		# self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % path))