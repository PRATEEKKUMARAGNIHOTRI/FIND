import sys, os

def up1(p):
	return os.path.split(p)[0]

main_dir = up1(up1(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(main_dir)
sys.path.append(os.path.join(main_dir, 'src'))
sys.path.append(os.path.join(main_dir, 'restyle_encoder'))