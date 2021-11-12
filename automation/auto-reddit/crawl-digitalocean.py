import os
import json

cmd = '''
curl 'https://6zheuvkj88-dsn.algolia.net/1/indexes/production_community_consolidated_newest/query?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%203.20.3&x-algolia-application-id=6ZHEUVKJ88&x-algolia-api-key=c5470567eae7fa1177d43222e18ba086'   -H 'Connection: keep-alive'   -H 'sec-ch-ua: "Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"'   -H 'accept: application/json'   -H 'DNT: 1'   -H 'content-type: application/x-www-form-urlencoded'   -H 'sec-ch-ua-mobile: ?0'   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'   -H 'sec-ch-ua-platform: "macOS"'   -H 'Origin: https://www.digitalocean.com'   -H 'Sec-Fetch-Site: cross-site'   -H 'Sec-Fetch-Mode: cors'   -H 'Sec-Fetch-Dest: empty'   -H 'Referer: https://www.digitalocean.com/'   -H 'Accept-Language: en-US,en;q=0.9,vi;q=0.8'   --data-raw '{"params":"query=%20&page=abc&hitsPerPage=50&facetFilters=%5B%5B%22feedable_language%3Aen%22%5D%2C%22published_tag_list%3Acde%22%2C%22item_type%3Atutorial%22%2C%22item_subtype%3A-tech_talk%22%5D&numericFilters=%5B%5D"}'   --compressed
'''
key = ["API", "Angular", "Ansible", "Apache", "Applications", "Automated Setups", "Backups", "Big Data",
       "Block Storage", "Books", "CDN", "CI/CD", "CMS", "CSS", "Caching", "CentOS", "CentOS 8", "Cloud Computing",
       "Conceptual", "Configuration Management", "Container", "Control Panels", "Custom Images", "DNS", "Data Analysis",
       "Databases", "Debian", "Debian 10", "Deployment", "Developer Education", "Development", "DigitalOcean",
       "DigitalOcean 1-Click Apps Marketplace", "DigitalOcean App Platform", "DigitalOcean Articles",
       "DigitalOcean Droplets", "DigitalOcean Managed Kubernetes", "DigitalOcean Managed Load Balancers",
       "DigitalOcean Managed PostgreSQL Database", "DigitalOcean Managed Redis", "DigitalOcean Spaces",
       "DigitalOcean Volumes", "Django", "Docker", "Drupal", "Elasticsearch", "Email", "FAQ", "Fedora", "Firewall",
       "Flask", "Flutter", "GatsbyJS", "Getting Started", "Git", "Glossary", "Go", "GraphQL", "HAProxy", "HTML",
       "High Availability", "IPv6", "Infrastructure", "Initial Server Setup", "Interactive", "Java", "JavaScript",
       "Kubernetes", "LAMP Stack", "LEMP", "Laravel", "Let's Encrypt", "Linux Basics", "Linux Commands",
       "Load Balancing", "Logging", "MEAN", "Machine Learning", "MariaDB", "Miscellaneous", "MongoDB", "Monitoring",
       "MySQL", "Networking", "Next.js", "Nginx", "NoSQL", "Node.js", "Object Storage", "Open Source", "PHP",
       "PHP Frameworks", "PostgreSQL", "Programming Project", "Python", "Python Frameworks", "Quickstart", "React",
       "Redis", "Rocky Linux", "Rocky Linux 8", "Ruby", "Ruby on Rails", "SQL", "SQLite", "Scaling", "Security",
       "Server Optimization", "Slack", "Solutions", "Spin Up", "System Tools", "Terraform", "TypeScript", "Ubuntu",
       "Ubuntu 16.04", "Ubuntu 18.04", "Ubuntu 20.04", "VPN", "VS Code", "Vue.js", "WordPress", "Workshop Kits",
       "Write for DO", "e-commerce"]

for i in range(0, 2):
    print(i)
    for el in key:
        result = os.popen(cmd.replace('abc', str(i)).replace('cde', el)).read()
        try:
            for element in json.loads(result)['hits']:
                f = open('link.txt', 'a')
                f.write(element['feedable_path'] + '\n')
        except Exception as e:
            print(e)
