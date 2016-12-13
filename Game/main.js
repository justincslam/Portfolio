var coin = 0;
var firstUpgradeCost = 0;
var firstUpgradeNumber = 0;
var secondUpgradeNumber = 0;

function buttonClick(number){
	coin = coin + number;
	document.getElementById("numberCoins").innerHTML = coin;
}

function buyUpgrade(number){
	var firstUpgradeCost = Math.floor(10 * Math.pow(1.1,firstUpgradeNumber));
	var secondUpgradeCost = Math.floor(10000* Math.pow(1.1,secondUpgradeNumber));
	if(coin >= firstUpgradeCost && number == 1){
		firstUpgradeNumber = firstUpgradeNumber + 1;
		coin = coin - firstUpgradeCost;
		document.getElementById('firstUpgradeNumber').innerHTML = firstUpgradeNumber;
		document.getElementById('numberCoins').innerHTML = coin;
	}
		else if (coin >= secondUpgradeCost && number == 2){
			secondUpgradeNumber = secondUpgradeNumber + 1;
			coin = coin - secondUpgradeCost;
			document.getElementById('secondUpgradeNumber').innerHTML = secondUpgradeNumber;
			document.getElementById('numberCoins').innerHTML = coin;
	}
var nextCost = Math.floor(10 * Math.pow(1.1,firstUpgradeNumber));
document.getElementById('firstUpgradeCost').innerHTML = nextCost;
}

window.setInterval(function(){
	buttonClick(firstUpgradeNumber);
	buttonClick(secondUpgradeNumber * 10);
},1000);

	
		
