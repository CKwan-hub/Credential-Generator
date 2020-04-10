# Credential-Generator

## **Generator for random userdata**
---

### Function

Tool can be used to generate random userdata emails and passwords en masse. JSON files are included with various length outputs, but any JSON file can be used for generation basis. 

The email is generated from the text included in the JSON (all words are above three characters in length), and consists of single or multiple words, and a random string of 0-4 digits. Then one of five available email suffixes are assigned. 

The password consists of a string of 6-12 characters consisting of ascii characters (both upper and lower care), digits, and special characters. 

---

### External Uses

Additionally, this tool can be used to pass the generated userdata to a URL's login fields for registration testing/debugging. 

Add a URL to the named field:

` url = '#'`

and rename the username and password fields that the login form accepts:

```
 requests.post(url, allow_redirects=False, data={
         '#': username,
         '#': password
     })
```

--- 

### Output

The generator outputs by default to output.txt file, and the terminal. To improve performance, output to a single source is advised. 

Additional generations will add to the output file if longer list of results are desired. 

---

### Options

The four included JSON files are compiled from literature of various lengths. 
Default is set to medium.

To change the output length and selection, change the following field to any of the JSON files:
`email_text = json.loads(open('medium_text.json').read())`

- "short_text.json" will output ~300 results.
- "medium_text.json" will output ~1,750 results. 
- "long_text.json" will output ~7,500 results.
- "longest_text.json will output ~100,000 results.

For a bonus, "million_text" will generate around 1.1 million results. 

