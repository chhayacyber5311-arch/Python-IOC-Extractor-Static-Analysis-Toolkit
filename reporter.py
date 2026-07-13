def print_report(results):
    print("\n======== IOC Reporter ==========")

    for category, values in results.items():
        print(f"\n[+] {category}")

        if isinstance(values,dict):
            for sub_category, sub_values, in values.items():
                print(f"      - {sub_category}:  {len(sub_values)}  found")


                for value in sub_values:
                    print(f"     {values}")

                else:
                    print(f"     {len(values)} found")


                    for value in values:
                        print(f"    - {value}")

        print("\n==============================================")