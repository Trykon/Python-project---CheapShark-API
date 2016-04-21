# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

f = open('CheapSharkAPI.html','w')

message = """
<html>

<head>
<title> Cheapshark API games search engine by Trykon</title>
<link rel="stylesheet" href="Bootstrap/bootstrap-3.3.5-dist/css/bootstrap.css" type="text/css"/>
<script>

$.ajax({
   url: "/path/to/your/script",
   success: function(response){
     //here you do whatever you want with the response variable
   }
});
</script>
</head>

<body>
<div class="row">
    <div class="col-md-2">
    </div>
    <div class="col-md-3">
        <p>Search for best deals</p>
        <form name="deals" action="">
        <table>
        <thead></thead>
        <tbody>
            <tr> <th>Title </th> <th><input type="text" id="sTitle" value=""><br></th> </tr>
            <tr> <th>Lowest price</th> <th><input type="text" id="sLowerPrice" value=""><br></th> </tr>
            <tr> <th>Highest price</th> <th><input type="text" id="sUpperPrice" value=""><br></th> </tr>
            <tr> <th>Sale only</th> <th><input type="checkbox" id="sOnSale" value=""></br></th> </tr>
            </tbody>
            </table>
            <p>Sort by:</p>
            <input type="radio" name="sort" id="DealRating" value="a">Deal rating<br>
            <input type="radio" name="sort" id="Title" value="b">Title<br>
            <input type="radio" name="sort" id="Price" value="c">Price<br>
            <input type="radio" name="sort" id="Release" value="d">Release<br>
        
        <input type="button" name="Sumbit" value="Submit" onClick="">
        </form>
        <p> Note: all fields are optional, fill only what you are intrested in.</p>
        
    </div>
    <div class="col-md-2">
        <p> OR </p>
    </div>
    <div class="col-md-3">
        <p>Search for your favourite games<p>
        <form name="games" action="">
        <table>
        <thead></thead>
        <tbody>
        <tr><th>Title</th> <th><input type="text" id="GameTitle" value=""></br></th></tr>
        </tbody>
        </table>
        <input type="button" name="Sumbit" value="Submit" onClick="">
        </form>
    </div>
    <div class="col-md-2">
    </div>
</div>
</body>
</html>
"""

f.write(message)

f.close()