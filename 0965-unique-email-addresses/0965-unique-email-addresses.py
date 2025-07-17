class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        final_email=set()
        for email in emails:
            local, domain=email.split("@")
            a_local=local.split("+")[0]
            b_local=a_local.replace(".", "")
            normal_email=b_local + "@" + domain

            final_email.add(normal_email)

        return (len(final_email))



        