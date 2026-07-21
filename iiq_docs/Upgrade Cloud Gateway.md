This page has for objective to explain how to perform the upgrade of the Cloud Gateway after deploying a new major version of IIQ or a patch.



gear Upgrade Cloud Gateway
Upload the new version of the IdentityIQ CG into the Cloud Gateway server.

Put the package into disk E:\Old

Extract the content of the package

Open the Services application

Windows > Services

cfdc3d0b-61c9-4f27-8448-a084f494b53c.png
Stop the Cloud Gateway Apache tomcat service.

Backup the current WEB-INF folder.



E:\identityiq-CloudGateway-DEV\apache-tomcat-9.0.60\webapps\CloudGateway\
into
E:\Backup\WEB-INF-DEV-<version_of_this_package>
Copy the WEB-INF folder from the new package into the current webapp CloudGateway. Override all existing files.

Warning From the backup, verify that the file iiq.properties has not been overridden by the upgrade. Otherwise, copy the iiq.properties file from the backup to the new WEB-INF folder.

Restart the service.

Make a Test connection in IIQ to confirm the correct deployment of the new version of the Cloud Gateway Check Mark.