function buttonFunction() {
  myFunction('30 Day SOLD');
  myFunction('60 Day SOLD');
  myFunction('30 Day NOT SOLD');
  myFunction('60 Day NOT SOLD');
}

function myFunction(targetSheet) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sourceSheet;
  var target = ss.getSheetByName(targetSheet);  
  
  if (targetSheet.indexOf('Day SOLD') >= 0) {
    sourceSheet = "Raw SOLD";
  } else {
    sourceSheet = "Raw NOT SOLD";
  } 
  
  var source = ss.getSheetByName(sourceSheet);
  target.getRange("A2:Z10000").clear();

  var source_range = source.getRange("A1:A");
  var values = source_range.getValues(); 
  var rowCount = values.length;
  var count = parseInt(rowCount);
  var source_range = source.getRange("A1:Q" + count);
  var pasteDate = ss.getSheetByName("Metrics");
  var Date = pasteDate.getRange("B2:B2").getValue();
  var Days = target.getRange("A1:A1").getValue();
  Date.setDate(Date.getDate() - Days);
  var values = source_range.getValues();
  var arrayLength = values.length;
  var headers = source.getRange("A1:Q1").getValues().pop();
  var newValues = [headers];
  
for (var i = 0; i < arrayLength; i++) {
    var row = values[i];
    var date = row[2];
  if (date >= Date){
    newValues.push(row);
  }

  
}
  
  var targetRange = target.getRange("A2:Q" + (newValues.length + 1));
  targetRange.setValues(newValues);
}
