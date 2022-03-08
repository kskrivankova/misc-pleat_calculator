import argparse

parser = argparse.ArgumentParser(description="Calculate pleat markings")
parser.add_argument("initial_length", nargs=1, type=float)
parser.add_argument("target_length", nargs=1, type=float)
parser.add_argument("-number_pleats", nargs=1, type=int)
parser.add_argument("-pleat_size", nargs=1, type=float)

args = vars(parser.parse_args())
print(args)
init_len = args.get("initial_length")[0]
target_len = args.get("target_length")[0]
num_pleats = args.get("number_pleats")[0] if args.get("number_pleats") else None
pleat_size = args.get("pleat_size")[0] if args.get("pleat_size") else None


if not init_len or not target_len:
	raise Exception("Missing arguments")

if num_pleats:
	if num_pleats < 1: raise Exception("Invalid pleat number")
elif pleat_size:
	num_pleats = target_len / pleat_size
else:
	raise Exception("Missing arguments")


total_pleat = init_len / num_pleats
vis_pleat = target_len / num_pleats
hid_pleat = total_pleat - vis_pleat

print(f"--{vis_pleat}--|-.-.{hid_pleat / 2}-.-.|-.-.{hid_pleat / 2}-.-.")

