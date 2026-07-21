from pathlib import Path

content = """\
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import sailpoint.object.Application;
import sailpoint.object.AttributeDefinition;
import sailpoint.object.ProvisioningPlan;
import sailpoint.object.ProvisioningPlan.AccountRequest;
import sailpoint.object.ProvisioningPlan.AttributeRequest;
import sailpoint.object.Schema;
import sailpoint.rule.Account;
import sailpoint.server.IdnRuleUtil;
import sailpoint.tools.GeneralException;

/* Throws a formatted exception including rule and application context */
private static void throwException(String message) {
    String messageLog = "ForcedException : " + applicationName + " : " + ruleName + "\\n" + message;
    throw new GeneralException(messageLog);
}

/* Rule name */
String ruleName = "ITAU-ISDS-BeforeProvisioning";

/* Application name */
String applicationName = application.getName();

/* Identity name */
String identityName = identity.getName();

/* Number of maximum attempts to generate a unique identifier */
int MAX_TRIES = 20;
if (application.getAttributeValue("c_maxTries") != null) {
    MAX_TRIES = Integer.parseInt(application.getAttributeValue("c_maxTries"));
}

/* Generate the next unique ID */
private String generateNextId(String identityName, String appName, String idxName, int maxTries) {
    String uniqueId = null;
    String idxValue = idn.getAccountAttribute("Contadores", "ISDS-" + idxName, "idx");
    if (idxValue == null || idxValue.trim().isEmpty()) {
        throwException("Attribute 'idx' for " + idxName + " is empty or null");
    }
    int id = Integer.parseInt(idxValue);
    for (int i = 1; i <= maxTries; i++) {
        id++;
        uniqueId = Integer.toString(id);
        if (idn.isUniqueLDAPValue(identityName, appName, idxName, uniqueId)) {
            return uniqueId;
        }
    }
    throwException("Unable to generate unique ID after " + maxTries + " attempts.");
}

List accReqs = plan.getAccountRequests();
for (AccountRequest accReq : accReqs) {
    if (accReq.getOperation().equals(AccountRequest.Operation.Create)) {
        String uidNumber = generateNextId(identityName, applicationName, "uidNumber", MAX_TRIES);
        String itauCartoesRedeUidNumber = generateNextId(identityName, applicationName, "itauCartoesRedeUidNumber", MAX_TRIES);
        accReq.add(new AttributeRequest("uidNumber", ProvisioningPlan.Operation.Set, uidNumber));
        accReq.add(new AttributeRequest("gidNumber", ProvisioningPlan.Operation.Set, uidNumber));
        accReq.add(new AttributeRequest("itauCartoesRedeUidNumber", ProvisioningPlan.Operation.Set, itauCartoesRedeUidNumber));
        accReq.add(new AttributeRequest("itauCartoesRedeGidNumber", ProvisioningPlan.Operation.Set, itauCartoesRedeUidNumber));
    }
}

/* return plan; */
"""

target = Path(r"C:\Projetos\Itau\Itau\src\ISC\ISDS\Rule - BeforeProvisioning - ISDS BeforeProvisioning.xml")
target.write_text(content, encoding="utf-8")
print(f"Done. Bytes written: {target.stat().st_size}")

