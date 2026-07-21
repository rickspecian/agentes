Upgrade IQService
Connect to the IQService server.

Launch a command prompt as Administrator

Stop the process



E:
cd IQService (Name is environment specific)
IQService.exe -k
Backup the folder IQService.

Backup the list of user saved in the service



IQService.exe -a list
Uninstall the IQService



IQService.exe -u
Extract new IQService zip file into IQService folder. Override all files

Install new IQService



IQService -i -n <service_name> -o 6060
Name of the service can be sam_dev, sam_int, sam_uat or sam_exp

Warning For DEV env, the port should be set to 6061.

Set the list of user with the backup list



IQService.exe -a <user1>;<user2>;...
Restart the service



IQService.exe -s
Test the new configuration in IIQ, make a test connection with an application using the IQService. Check Mark