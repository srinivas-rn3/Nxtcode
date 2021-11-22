
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function() {
  if(this.readyState === 4) {
    console.log(this.responseText);
  }
});

xhr.open("POST", "https://rds.us-east-1.amazonaws.com/?Action=CreateDBSubnetGroup&DBSubnetGroupDescription=Subnet-3&DBSubnetGroupName=test-subnetgroup&SignatureMethod=HmacSHA256&SignatureVersion=4&SubnetIds.member.1=subnet-0714345be5056fcb4&SubnetIds.member.2=subnet-060b71185a7a6d0a5&Version=2014-09-01&X-Amz-Date=20211115T154152Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZQV225CBEIXKKIWS%252F20211115%252Fus-east-1%252Frds%252Faws4_request&X-Amz-SignedHeaders=action%253Bhost%253Bmaxrecords%253Bsignaturemethod%253Bsignatureversion%253Bversion%253Bx-amz-algorithm%253Bx-amz-credentia%253Bx-amz-signedheaders&X-Amz-Signature=9a21b6bf027681286166ffae863ed448dad7f197c7a661aaf39ecfcffc1da2dc");
xhr.setRequestHeader("MaxRecords", "10");
xhr.setRequestHeader("SignatureMethod", "HmacSHA256");
xhr.setRequestHeader("SignatureVersion", "4");
xhr.setRequestHeader("X-Amz-Algorithm", "AWS4-HMAC-SHA256");
xhr.setRequestHeader("Action", "DescribeDBSubnetGroups");
xhr.setRequestHeader("version", "2014-09-01");
xhr.setRequestHeader("X-Amz-Credentia", "AKIAZQV225CBEIXKKIWS/654300604546/us-east-1/rds/aws4_reques");
xhr.setRequestHeader("X-Amz-SignedHeaders", "content-type;host;user-agent;x-amz-content-sha256;x-amz-date");

xhr.send();