# Path of the file to import"
file_path = "D:\OneDrive\OneDrive - Varadise Ltd\Isma\Change Piles Color\Spline\dxf.dxf"

# Command for the Rhino Command line to be executed including the path
Command = '_-Import "'+ file_path + '" Objects Enter 0,0,0 1 0'

# Run the Command
rs.Command(Command)
