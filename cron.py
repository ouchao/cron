#!/bin/env python
import time
import os,sys
from plan import Plan


def crontab(j):
	date	=time.strftime('%Y-%m-%d-%H%M%S')

	if not j.has_key('id') :
		return -1
	elif not j.has_key('action') :
		return -2

	
	j['cmd']   = j.has_key('cmd')    and j['cmd']   or ''
	j['every'] = j.has_key('every')  and j['every'] or ''
	j['at']    = j.has_key('at')	 and j['at']	or ''

	jobname	='job%s-%s'%(str(j['id']),j['every'])
	logsdir	='%s/Logs/cronlogs/%s'%(os.getcwd(),jobname)

	try:
		os.makedirs(logsdir)
	except Exception,e:
		pass


	exec_command='PATH=$PATH && %s'%j['cmd']
	output      = dict(stdout='%s/%s.stdout.log'%(logsdir,jobname), stderr='%s/%s.stderr.log'%(logsdir,jobname) )

	cron = Plan(name='job'+str(j['id']))
	if j.has_key('at') :
		r=cron.command(exec_command,every=j['every'],at=j['at'],output=output,)
	else:
		r=cron.command(exec_command,every=j['every'],output=output,)

	cron.run(j['action'])
	return True

if __name__ == '__main__':
	#job1={'id':1,'cmd':'date','every':'2.day','action':'update','at':'hour.12 minute.15 minute.45'}
	job2={'id':2,'cmd':'/home/qilong/python/cron/1.sh','every':'1.hour','action':'update','at':'minute.10'}
	crontab(job2)

	#print job2
	#job2=sys.argv[1]
	#crontab(eval(job2))
