with open(os.path.join(setting.path_report,file_scrape_data),'w',encoding='utf-8') as f:
  for record in recordsall:
    line = '\t'.join(str(item) for item in record)
    f.writelines(line +'\n')
