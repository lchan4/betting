
//Sets button as event handler on window load

window.onload = function() {
	let button = document.getElementById("submitButton");
	button.onclick = submitHandler;
}

function submitHandler() {

	var betSpread = Number(document.getElementById("betSpread").value);
	var betOdds = Number(document.getElementById("betOdds").value);
	var closeSpread = Number(document.getElementById("closeSpread").value);
	var closeOdds = Number(document.getElementById("closeOdds").value);

  let radio = document.getElementsByName('sport');
	let sport = displayRadioValue(radio);

	let betP = percent(betOdds);
	let closeP = percent(closeOdds);

	let push = pushData(sport);

	let result = clv(betSpread,betP,closeSpread,closeP,push);

	document.getElementById("answer").innerHTML = "CLV is " + result + "%.";
}

// get radio button value

function displayRadioValue() {
		let radio = document.getElementsByName('sport');

		for(i = 0; i < radio.length; i++) {
				if(radio[i].checked) {
					return radio[i].value
				}
		}
}
// converts odds to breakeven percents

function percent(odds) {

	let p = 0;

	if (odds < 0) {
		p = odds / (odds - 100);
	} else {
		p = 100 / (odds + 100);
	}

	return p;
}

// sets push data to correct sport

function pushData(sport) {

	if (sport === "NBA" ) {
		return [0, 0.0227/2, 0.0403/2, 0.0383/2, 0.0348/2, 0.0437/2, 0.0416/2, 0.0411/2, 0.042/2, 0.0476/2, 0.0416/2, 0.0387/2, 0.0351/2, 0.0385/2, 0.0349/2, 0.033/2, 0.0499/2, 0.0299/2, 0.0341/2, 0.0333/2, 0.0227/2];
	} else if (sport === "NFL") {
		return [0, 0.025/2, 0.02/2, 0.098/2, 0.03/2, 0.017/2, 0.034/2, 0.057/2, 0.021/2, 0.009/2, 0.049/2, 0.022/2, 0.004/2, 0.013/2, 0.049/2, 0.015/2, 0.035/2, 0.046/2];
	}
}

// calculates CLV from given information

function clv(betS,betP,closeS,closeP,push) {

	let a = 0;
	let b = 0;
	let adv = 0;
	let clv = 0;

	if (Math.abs(betS) > Math.abs(closeS)) {
		a = betS;
		b = closeS;
	} else {
		a = closeS;
		b = betS;
	}

	if ((a + 0.1) / (b + 0.1) < 0) {
		while (a != 0) {
			adv += push[Math.floor(Math.abs(a))];

			if (a > 0) {
				a -= 0.5;
			} else {
				a += 0.5;
			}
		}
		while (b != 0) {
			adv += push[Math.floor(Math.abs(b))];

			if (b > 0) {
				b -= 0.5;
			} else {
				b += 0.5;
			}
		}
	} else {
		while (a != b) {
			adv += push[Math.floor(Math.abs(a))];

			if (a > b) {
				a -= 0.5;
			} else {
				a += 0.5;
			}
		}
	}

	if (betS > closeS) {
		closeP += adv;
	} else {
		closeP -= adv;
	}

	clv = 100 * (closeP - betP) / betP;

	return clv.toPrecision(3);
}
