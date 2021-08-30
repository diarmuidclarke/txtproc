import sys
import os
import pprint

def main():
	cwd =  os.getcwd()
	tagloc = {}

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
				'Document number;',
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
	txt_full = f.read()

	for tag in tag_expressions.keys():
		expr_list = tag_expressions[tag]
		print('T:' + tag + ' >>> ' + str(expr_list))
		li = sys.maxsize

		for exp in expr_list:
			i = txt_full.lower().find(exp.lower())
			if i <0:
				continue
			if i < li:
				li = i
				tagloc[i]=tag

	pp = pprint.PrettyPrinter()
	pp.pprint(tagloc)

	get_title(txt_full, tagloc)

def get_title(txt_full, tagloc):
	title = None
	idx = [i for i in tagloc.keys() if tagloc[i] == 'title']
	txt2search = get_txt_to_search(idx[0], txt_full, tagloc)
	print('txt2srch>>>' + txt2search)
	return title

def get_txt_to_search(idx, txt_full, tagloc):
	next_tag = False
	idx_start = idx
	idx_end = -1
	txt_to_search = ''
	for tag in tagloc.keys():
		if next_tag:
			idx_end = tag
			break
		if tag == idx:
			next_tag = True

	if next_tag:
		txt_to_search = txt_full[idx_start:idx_end]
	else:
		txt_to_search = txt_full[idx_start:]

	return txt_to_search




if __name__ == '__main__':
	main()
