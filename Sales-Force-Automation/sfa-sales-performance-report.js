const d3 = require('d3');
const fs = require('fs');
const sqlite3 = require('sqlite3');

// Connect to the database
const db = new sqlite3.Database('sales.db');

// Retrieve sales performance data from the database
let salesPerformanceData = [];
db.all("SELECT s.name, SUM(sp.amount) as total_sales, sq.amount as sales_quota FROM salespeople s JOIN sales_performance sp ON s.salesperson_id = sp.salesperson_id JOIN sales_quotas sq ON s.salesperson_id = sq.salesperson_id GROUP BY s.salesperson_id", (err, rows) => {
    if (err) {
        throw err;
    }
    salesPerformanceData = rows;
});

// Create an HTML template with a table to display the sales performance data
const html = `
<html>
  <head>
    <style>
      table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
      }

      td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
      }

      th {
        background-color: #dddddd;
      }
    </style>
  </head>
  <body>
    <h1>Sales Performance Report</h1>
    <table>
      <tr>
        <th>Name</th>
        <th>Total Sales</th>
        <th>Sales Quota</th>
        <th>Achieved Quota</th>
      </tr>
      ${d3.select('body')
        .selectAll('tr')
        .data(salesPerformanceData)
        .enter()
        .append('tr')
        .html(d => {
          return `
            <td>${d.name}</td>
            <td>${d.total_sales}</td>
            <td>${d.sales_quota}</td>
            <td>${d.achieved_quota ? 'Yes' : 'No'}</td>
          `;
        })}
    </table>
  </body>
</html>
`;

// Write the HTML template to an HTML file
fs.writeFileSync('sales_performance_report.html', html);
