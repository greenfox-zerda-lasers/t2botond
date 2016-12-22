var mysql = require('mysql');

var connection  = mysql.createConnection({
  host: 'localhost',
  user:'root',
  password:'6025',
  database:'bookstore'
});

connection.connect(function(error){
  if (error) {
    console.log('jajjjj');
  } else {
    console.log('sikerult');
  }
}
);
connection.query('SELECT * FROM author;', function(err, rows){
  console.log('Data received from Database:/n');
  console.log(rows);
});
connection.query('select book_name, aut_name, cate_descrip, pub_name, book_price from book_mast join author on book_mast.aut_id=author.aut_id join category on book_mast.cate_id=category.cate_id join newpublisher on book_mast.pub_id=newpublisher.pub_id', function(err, rows){
  if(err) {
    console.log(err.toString());
    return;
  }
  console.log('Data received from Database:/n');
  console.log(rows);
})
