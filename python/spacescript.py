
string = (
"██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗\n"
"██║     ██║████╗  ██║██║   ██║╚██╗██╔╝\n"
"██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝\n"
"██║     ██║██║╚██╗██║██║   ██║ ██╔██╗\n"
"███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗\n"
"╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝\n"
"██╗  ██╗███████╗██████╗ ███╗   ██╗███████╗██╗\n"
"██║ ██╔╝██╔════╝██╔══██╗████╗  ██║██╔════╝██║\n"
"█████╔╝ █████╗  ██████╔╝██╔██╗ ██║█████╗  ██║\n"
"██╔═██╗ ██╔══╝  ██╔══██╗██║╚██╗██║██╔══╝  ██║\n"
"██║  ██╗███████╗██║  ██║██║ ╚████║███████╗███████╗\n"
"╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝"
)
list = [x for x in string]
pro = "".join(list).replace(" ", ":")
with open("shadows.txt", "w") as x:
	x.write(pro)