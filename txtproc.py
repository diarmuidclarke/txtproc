import sys
import os

def main():
	cwd =  os.getcwd()

	tag_expressions = {
		'date' :
			[
				'date',
				'date#5'
			],
		'docnum' :
			[
				'Document ID:',
				'Document ID:#10',
				'Document number'
			],
		'issue' :
			[
				'Issue',
				'issue#7'
			],
		'author' : 
			 [
				'author',
				'authors',
				'author#15'
			],
		'title' : 
			[
				'title',
				'title#20'
			],
		'summary':
			[
				'Summary',
				'Summary#30',
			],
		'approvedby':
			[
				'Approved by',
				'approved by:',
			],
		'signedby':
			[
				'signed by',
				'Signed by:',
				'Signed by:#55',
			],
		'export' :
			[
				'This data is export controlled',
				'pl9009.c',
			],
		'toc' :
			[
				'table of contents',
				'contents'
			],
			
	}
	
	# analyse tag order, and tag expressions
	f = open(cwd + '/sample.txt','r')
	for tag in tag_expressions.keys():
		expr_list = tag_expressions[tag]
		print('T:' + tag + ' >>> ' + str(expr_list))


if __name__ == '__main__':
	main()
