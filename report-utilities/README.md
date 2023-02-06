## Reporting Utilities
Reports provide information to a firm's management to support well-informed optimized business decision-making. 

This information comes from two sources, internal and external. Internal sources provide information to monitor the performance of internal operations. External sources provide information to monitor performance of competing firms (business intelligence). 

### Control Break Reports

The traditional paper 'control break report' employs 'control breaks' to provide line-items and sub-totals that summarize information essential to decision-making. Reports are created for the various business units and levels of internal management within a firm to support them in meeting their objectives: 

"In computer programming a control break is a change in the value of one of the keys on which a file is sorted which requires some extra processing For example, with an input file sorted by post code, the number of items found in each postal district might need to be printed on a report, and a heading shown for the next district. Quite often there is a hierarchy of nested control breaks in a program, e.g. streets within districts within areas, with the need for a grand total at the end. Structured programming techniques have been developed to ensure correct processing of control breaks in languages such as COBOL and to ensure that conditions such as empty input files and sequence errors are handled properly. With fourth generation languages such as SQL, the programming language should handle most of the details of control breaks automatically." (Source: [Wikipedia](https://en.wikipedia.org/wiki/Control_break)) 

First written in COBOL, Control break reports can also be [written in Python's Pandas](https://github.com/jonfernq/SimpleERP/blob/main/report-utilities/pandas-control-break.py) which can also be used to create data visualizations to augment basic reports. The code snippet/template linked to above produces the general pattern of a control break report: 

![control_break_report_](https://user-images.githubusercontent.com/68504324/217078146-541b20ac-a5b0-4adc-8171-b35064b19507.jpg)
