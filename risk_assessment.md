1. Assets, Vulnerabilities and Possible Consequences
Asset	Vulnerability	Possible Consequence
1. Central student records server	Guest network users can access the records server.	Unauthorized users may access, modify, or delete confidential student records, causing data leakage, loss of integrity, and disruption of services.
2. Student records and files transferred between campuses	File transfers are unencrypted.	Attackers could intercept the files and read or modify sensitive student information while it is being transferred.
3. IT staff accounts and systems	Weak staff passwords and outdated software.	Attackers may guess or compromise staff accounts or exploit known software vulnerabilities, potentially gaining unauthorized access to systems and sensitive information.
Additional Security Observation
The repeated attempts to reach the server from an unfamiliar external address indicate possible unauthorized access attempts. This increases the likelihood that the vulnerabilities could be actively exploited.
2. Risk Ranking
The risks are ranked according to likelihood and impact.
Rank	Risk	Likelihood	Impact	Reason
1	Unauthorized access to the student records server through the guest network	High	High	The guest network already provides a potential path toward a highly sensitive server. If network segmentation and filtering are weak, unauthorized users could reach the records server.
2	Interception of unencrypted file transfers	High	High	Files are transferred without encryption, allowing someone who can monitor the network traffic to potentially read or alter sensitive student information.
3	Compromise through weak passwords and outdated software	High	High	Weak passwords can be guessed or attacked, while outdated software may contain known vulnerabilities. The repeated external connection attempts make attempted exploitation a realistic concern.
Risk Assessment Explanation
The central student records server has particularly high importance because it contains sensitive student information. Unauthorized access could affect confidentiality, integrity, and availability.
Unencrypted file transfers create a significant confidentiality risk because information can potentially be captured while travelling between the two campuses.
Weak passwords and outdated software increase the attack surface of the institution. The observed repeated attempts from an unfamiliar external address should therefore be investigated and monitored.
3. Recommended Controls
Risk 1: Unauthorized Guest Network Access
Recommended control: Network segmentation and firewall traffic filtering
The guest network should be isolated from the internal network containing the student records server. Firewall rules should deny guest-network traffic to the records server while allowing only authorized internal systems and users to communicate with it.

Figure 1 — Guest network traffic is blocked at the firewall; only authorized internal systems can reach the server.
This reduces the possibility of unauthorized users reaching the server.
Risk 2: Unencrypted File Transfers
Recommended control: Use encrypted file-transfer protocols
The institution should replace unencrypted file transfers with a secure protocol such as SFTP (SSH File Transfer Protocol) or another appropriately secured transfer mechanism.
Encryption protects the confidentiality and integrity of files while they are travelling between campuses.

Figure 2 — Files move between campuses over an encrypted SFTP connection.
Risk 3: Weak Passwords and Outdated Software
Recommended control: Strong authentication and regular patching
Staff accounts should use strong, unique passwords and, where possible, multi-factor authentication (MFA). Operating systems and applications should also be regularly updated with security patches.
A password policy should require:
Strong and sufficiently long passwords
Unique passwords for each account
No sharing of staff passwords
Regular monitoring for compromised accounts
MFA for important administrative accounts
The IT team should maintain an update schedule to ensure that outdated software is patched or replaced.
4. Summary
The security review identified three major risks:
Guest network access to the central records server
Unencrypted file transfers between campuses
Weak passwords and outdated software
Summary of Risks and Controls
Risk	Recommended Control
Guest network access to the central records server	Network segmentation and firewall traffic filtering
Unencrypted file transfers between campuses	Encrypted file-transfer protocol (e.g., SFTP)
Weak passwords and outdated software	Strong authentication, MFA, and a regular patch schedule
The most important security improvements are to isolate the guest network using firewall rules, encrypt file transfers, and strengthen authentication while keeping software patched.
The repeated external connection attempts should also be logged and investigated to determine whether they represent unauthorized scanning or attempted intrusion.
