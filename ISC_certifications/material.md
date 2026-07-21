1.1 identify valid search queries
1.2 create and schedule search reports -> search -> define search -> save search -> select saved search -> make a subscription -> select interval -> receive 2 links in mailbox, 1 to download and other to execute the search in isc
1.3 know how to auth to the rest api -> pass the tenant, client id and secret into a collection (example), sailpoint collection scripts will do the auth steps
1.4 diff ways to monitoring provisioning activities -> by the default provisioning activity report, account activity tab in search or viewing a list of manual provisioning tasks
1.5 know diff security administrations ?
1.6 understand the use cases surrounding event triggers -> review all event triggers
1.7 ambiguous question, its possible to be the idp (identity provider) or auth steps in identity profiles. IDP its a global configuration, id profiles ables to configure a direct connection with a connector w/pass through auth (PTA) like AD, EntraID or WebServices - https://documentation.sailpoint.com/saas/help/common/pta.html
1.8 recognize diff components in a wf -> Triggers, Operations and Actions
1.9 know how to backup and restore configurations -> with configuration hub its possible to create backups and rollback actions, also its possible to schedule backups.
2.1 understand virtual appliances and know what they are -> A VA is a linux-based virtual machine that connects to your sources and apps using sailpoint apis, connectors and integrations. The VA is provided as a virtual disk image. VA is a man-in-the-middle communication between sailpoint cloud (tenant) and network/firewall protected applications
2.2 monitor the health of virtual appliances -> https://documentation.sailpoint.com/saas/help/va/manage_va.html#monitoring-va-health
2.3 perform basic troubleshooting of virtual appliances -> https://community.sailpoint.com/t5/IdentityNow-Connectors/Virtual-Appliance-Troubleshooting-Guide/ta-p/78735
3.1 understand the use of identity profiles -> separate user types and specific identity attributes based on company rules, employees, non-employees...
3.2 Understand the authentication options in an identity profile  -> User Name & Password - Users in this identity profile sign in to Identity Security Cloud with the username and password created during their registration process. | Directory Connection - Users loaded from the identity profile sign in using the password associated with the source selected from the Authentication Source dropdown list. This type of authentication is also referred to as pass-through authentication. | Users in this identity profile sign in using a mobile authenticator application such as Google Authenticator or Duo Mobile. Admins will still be required to use MFA even if this checkbox is disabled on the identity profile.
3.3 know identity attribute mappings and how they function within an identity profile -> https://documentation.sailpoint.com/saas/help/setup/identity_profiles.html#defining-identity-profile-attributes
3.4 recognize which options are avaliable for configuring mappings in an identity profile -> after defining a id attribute or create one, its possible to select the source, source attribute and a transform. Transforms are not mandatory*
3.5 Know lifecycle states and their use cases -> (https://documentation.sailpoint.com/saas/help/provisioning/lifecycle.html) Lifecycle states describe a user's status in the organization, which you can use to drive access changes for your users. For example, when a new employee joins your company, Identity Security Cloud can grant them the required access for active employees. When someone leaves the organization, their access can be automatically revoked or their source accounts disabled.
3.6 Understand the different provisioning options within a lifecycle state -> its possible to enable, disable or delete  all or selected user accounts (delete only if long_term is selected), also its possible to revoke all access, grant access profiles and send e-mail notifications. OBS1: For revoke acess option, all access items are revoked except those provisioned from birthright roles and access profiles provisioned from the current lifecyclestate. All removal approval steps will be bypassed. OBS2: we have 3 identity state options, ACTIVE, INACTIVE SHORT TERM and INACTIVE LONG TERM, between inactive statuses, the diff is that long-term is mostly used for leaver users (enables the delete account option)
3.7 Describe the purpose of the cloud lifecycle state attribute -> this attribute is setted to define the lifecycle state of a identity. Identities can be assigned to one clstate at a time.
4.1 Understand how provisioning is triggered -> It can be initiated by users through actions such as access requests, certifications, or manager requests, or through automated configurations. Automated configurations include role assignments and lifecycle states that keep user access aligned with their business requirements.
4.2 Know the different components of source provisioning -> related as 'provisioning' we have: create accounts, enable/disable accounts, delete accounts, grant or revoke access. related to specific method 'create' we have some items defined as 'account attribute mappings' that makes the create provisioning policy. Those are: Identity Attribute, Generator, Static, disabled, rules and custom transform. OBS: custom transforms and rules (rules are set) are make through api only.
4.3 Understand what the possible provisioning channels are and their high-level use case -> In SailPoint IdentityNow, provisioning can be executed through different methods or “channels” depending on how your sources are configured: Direct provisioning, File based provisioning, Service Desk integration and Web Services / API Provisioning ->
1. Direct Provisioning (Direct Connect)
Description: Real-time provisioning through connectors that communicate directly with target systems
Connection Type:directordirectConnect: true
Use Case:
Applications that support API-based provisioning
Systems where real-time access changes are critical
Sources with web services or REST APIs (e.g., Active Directory, LDAP, ServiceNow, Workday)
When you need immediate account creation, updates, or deletions
Requirements: Requires a Virtual Appliance (VA) or Cloud Gateway for on-premise systems, or cloud-to-cloud connections for SaaS applications
2. File-Based Provisioning
Description: Provisioning through file uploads/downloads
Connection Type:connectionType: "file"orfileUpload: true
Use Case:
Legacy systems without API capabilities
Batch provisioning operations
Systems that only support file-based imports
When you need to provision to systems that don’t have direct connectivity
Process: IdentityNow generates provisioning files that are uploaded to or retrieved from the target system
3. Service Desk Integration (SDIM)
Description: Provisioning through ticketing systems like ServiceNow
Types:ServiceNowSDIM,ServiceNow
Use Case:
When provisioning requires manual approval or human intervention
Systems that require change management processes
Applications where automated provisioning isn’t possible or desired
Compliance-heavy environments requiring audit trails
Process: Provisioning requests create tickets in the service desk system, which are then fulfilled manually or semi-automatically
4. Web Services / API Provisioning
Description: Cloud-native provisioning through REST APIs
Use Case:
Modern SaaS applications with REST APIs
Cloud-to-cloud integrations
Applications supporting SCIM protocol
No on-premise infrastructure required
4.4 Understand how to enable logging and different logging levels for specific connectors -> those sources has specifics UI pages that enable particular logs, example: EntraID or GCP. Also, its possible to enable VA ccg debug log level to view specific source logs
4.5 Know which objects to search on to troubleshoot provisioning errors -> identity specific events tab, Search event tab or Search account activity tab, also we wave the provisioning activity report. And ccg.log to trace...
5.1 Recognize how user levels grant specific capabilities -> User levels are sets of permissions within Identity Security Cloud that administrators can grant to users. Generally, users cannot grant themselves user level permissions - only Admins can grant or remove user levels. If you configure your tenant to enable non-Org Admins to manage Identity Security Cloud user level entitlements, Role Admins and Source Admins are also able to elevate privileges. Users can be granted multiple user levels and will have the combined access of all levels assigned to them.
5.2 Understand the basics of entitlements -> Entitlements are the access rights an account has on a source. They're a key part of identity governance and an important way of quantifying access. They can be assigned to access profles, roles and directly requested in access requests
5.3 Understand different types of access that SailPoint supports -> Entitlements, Access profiles and roles. Applications are not access types, just a bundle of applications access items. For roles, we have some types: 'Flat role' -> roles that just contains entitlements, 'hybrid roles' -> roles contains access profiles and entitlements, and 'Two-tier roles' are roles that contains only access profiles.
5.4 Know how automated role assignments work -> based on assignment criteria, provision entitlements and access profiles. If the user no longer meets the criteria, isc desprovisions the role. Revoking roles does not remove accounts. Roles can be assigned by a dynamic criteria or adding users in a static list. with criteria, we have some options: Criteria groups type[Account attribute, Entitlement, identity Attribute] for account attributes we need to pass the source and the schema attribute. In operations we have [equals, not equals, contains, not contains, starts with, ends with]; in identity attributes we just get the attribute name, and the operations are the same of account attribute. For entitltements, we have to pass the source and entitlement. For operations we just have equals and not equals.
5.5 Troubleshoot access management errors -> search, reports (for requested access). For automatic access, user event tab. OBS: Automated role provisioning requests which fail with a retryable error are automatically retried once per hour, up to 3 times. Identity Security Cloud automatically recognizes some provisioning error messages from source connectors, such as ConnectException and NoRouteToHostException, as retryable errors. When Identity Security Cloud receives a retryable error during provisioning, it will retry the action once per hour, up to 3 times. Although the action is scheduled to run after 60 minutes, it may be delayed due to other work items in your tenant's queue.
6.1 Recognize the basic steps of access requests -> users submit access requests -> reviewers approve or deny access requests -> if approved, the access is provisioned -> if an expiration date was specified, the system initiates revocation as scheduled
6.2 Understand work reassignment  -> Work Reassignment allows access request reviews, certifications, and manual provisioning tasks assigned to a user to be reassigned to a different user. Use cases are: Temporarily redirecting work for users who are out of office, such as on vacation or sick leave. Or permanently redirecting work for users who should not be assigned these tasks at all, such as senior executives or service identities. In reassigns we can define to reassign all items types (Access requests, certifications, tasks or generic approvals)
6.3 Understand the approval flow  -> sequencial approvers, not parallel. the approval flow its customized in each access profile/role/entittlement and we can use: 1 all owners, 1 primary owner, 1 aditional owners, 1 manager, 1 app owner, 1 source owner,
6.4 Know the lifecycle of a certification -> certification phases -> "generation, preview, active, end"
6.5 Understand the different types of certifications that are supported in Identity Security Cloud -> search based certifications [role composition, identities, access items, uncorrelated accounts, machine accounts]. Filter based certifications -> [manager campaign, source owner campaign]
6.6 Understand the different types of policies that are supported in Identity Security Cloud -> general policies and sod policies
7.1 Recognize the difference between aggregation types -> entitlement aggregations, account aggregations, (delta aggregations are used to aggregate only the items that hava changed, example: normal aggregations pull 1000 users but only 3 users have changed. Delta only pull 3). https://documentation.sailpoint.com/saas/help/accounts/loading_data.html#aggregation-methods
7.2 Know the process for obtaining account and entitlement information -> defining, configuring schemas and aggregation.
7.3 Understand uncorrelated accounts -> These are accounts that did not meet the criteria for correlation between identity attribute and account attribute. They are generally classified as uncorrelated accounts / phantom identities.
7.4 Understand the account deletion process and how the account deletion affects the aggregation process -> Account deletion represents the percentage of deleted accounts that aggregation can remove from the source. In sources with small numbers of accounts, the Percentage of Deleted Accounts Allowed value will be rounded to the nearest whole account. If the percentage you select does not round to at least 1 account, the aggregation will only be canceled if 100% of the accounts on the source would be deleted by the aggregation. Ensure you always set a Percentage of Deleted Accounts Allowed value to represent at least 1 account.For example, if you are aggregating a source with 10 accounts, set the Percentage of Deleted Accounts Allowed to at least 5%. This will be rounded to 10%, or 1 account, and the aggregation will be canceled if 1 or more accounts would be deleted during the aggregation.
7.5 Know the main (generic) different types of connectors -> Delimited File, JDBC, Web Services, Generic, LDAP, SCIM 1.1, SCIM 2.0, SCIM 2.0 saas, Web service saas
7.6 Know how to search for source errors - aggregation history, provision analysis (mencioned above), test connections, ccg.log... source satus messages -> alert icon in UI or email notification for admins
7.7 Understand the purpose of a source -> You will use sources to load user data from applications, databases, or directory management systems into Identity Security Cloud. SailPoint provides connectors to collect user accounts and access rights from those systems and associate them with the source definition.
8.1 Define and understand IGA ->identity governance and administration, core: identity governance and identity administration
8.2 Understand compliance -> It involves all the processes of monitoring an organization's systems, access, and policies, ensuring users comply with necessary requirements. ISC provides two specific features to compliance: Certifications allow you to review the access that your user's hold and make changes as needed AND Policies can alleviate unwanted data and access conditions
8.3 Compare and contrast authentication and authorization -> authentication verifiies who you are/identity, authorization determines what you hava access to (related to permissions).
8.4 Understand the concept of federation -> Network Identity Federation is a system that enables users to use a single digital identity to access services across multiple, independent security domains. It eliminates the need for users to create and manage separate credentials for each application or network. This approach streamlines user experience and enhances security by centralizing identity management.
8.5 Know methods of authentication -> saml, oauth, oidc