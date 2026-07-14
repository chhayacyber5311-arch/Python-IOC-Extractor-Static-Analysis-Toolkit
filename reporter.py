# Creating new function to print report into text
def build_text_report(results):
    lines=[]
    lines.append(f"\n=============IOC REPORTER==============")

    for category, values in results.items():
        lines.append(f"\n[+]  {category}")

        if isinstance(values, dict): 
           for sub_category, sub_values in values.items():
             lines.append(f"   - {sub_category}: {len(sub_values)}  found")
 
             for value in sub_values:
                  lines.append(f"    -  {value}")

        else:
            lines.append(f"  {len(values)} found")
        

            for value in values:
              lines.append(f"   -  {value}")

    lines.append("\n============================================")
    return "\n".join(lines)

def print_report(results):
    print(build_text_report(results))
   
