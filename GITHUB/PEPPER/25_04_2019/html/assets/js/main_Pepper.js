var tableenseignants = document.getElementById('table-enseignants');

$.ajax({
	url: "http://tp-epu.univ-savoie.fr/~picardap/Pepper PHP/Enseignants.php",
	crossDomain: true,
	type: "GET",
	success: function (data) {
		var json = JSON.parse(data);
		for (var i = 0; i < json.length; i++) {
			tableenseignants.innerHTML += "<tr>" +
			"<td class=\"column1\">" + json[i].civilite + " " + json[i].nom + " " + json[i].prenom + "</td>"
			+ "<td class=\"column2\">" + json[i].description + "</td>"
			+ "<td class=\"column3\">Salle " + json[i].localisation + "</td>"
			+"<td class=\"column4\"><a onclick=\"session.raiseEvent('go_to_room/Room"+ json[i].localisation + "', true);\" href=\"#\" class=\"button\">Go &#x25B6;</a></td>"
			+ "</tr>";
		}
	},
	error: function(error) {
		showError(JSON.stringify(error))
	}
})

var tablepersonnelsadministratif = document.getElementById('table-personnels-administratif');

$.ajax({
	url: "http://tp-epu.univ-savoie.fr/~picardap/Pepper PHP/PersonnelsAdministratif.php",
	crossDomain: true,
	type: "GET",
	success: function (data) {
		console.log(data);
		var json = JSON.parse(data);
		for (var i = 0; i < json.length; i++) {
			tablepersonnelsadministratif.innerHTML += "<tr>" +
			"<td class=\"column1\">" + json[i].civilite + " " + json[i].nom + " " + json[i].prenom + "</td>"
			+ "<td class=\"column2\">" + json[i].description + "</td>"
			+ "<td class=\"column3\">Salle " + json[i].localisation + "</td>"
			+"<td class=\"column4\"><a onclick=\"session.raiseEvent('go_to_room/Room"+ json[i].localisation + "', true);\" href=\"#\" class=\"button\">Go &#x25B6;</a></td>"
			+ "</tr>";
		}
	},
	error: function(error) {
		showError(JSON.stringify(error))
	}
})

var tableautrepersonnels = document.getElementById('table-autre-personnels');

$.ajax({
	url: "http://tp-epu.univ-savoie.fr/~picardap/Pepper PHP/AutrePersonnels.php",
	crossDomain: true,
	type: "GET",
	success: function (data) {
		console.log(data);
		var json = JSON.parse(data);
		for (var i = 0; i < json.length; i++) {
			tableautrepersonnels.innerHTML += "<tr>" +
			"<td class=\"column1\">" + json[i].civilite + " " + json[i].nom + " " + json[i].prenom + "</td>"
			+ "<td class=\"column2\">" + json[i].description + "</td>"
			+ "<td class=\"column3\">Salle " + json[i].localisation + "</td>"
			+"<td class=\"column4\"><a onclick=\"session.raiseEvent('go_to_room/Room"+ json[i].localisation + "', true);\" href=\"#\" class=\"button\">Go &#x25B6;</a></td>"
			+ "</tr>";
		}
	},
	error: function(error) {
		showError(JSON.stringify(error))
	}
})

var tablesallesadministrative = document.getElementById('table-salles-administrative');

$.ajax({
	url: "http://tp-epu.univ-savoie.fr/~picardap/Pepper PHP/SallesAdministrative.php",
	crossDomain: true,
	type: "GET",
	success: function (data) {
		var json = JSON.parse(data);
		for (var i = 0; i < json.length; i++) {
			tablesallesadministrative.innerHTML += "<tr>" +
			"<td class=\"column1\">" + json[i].localisation + "</td>"
			+ "<td class=\"column2\">" + json[i].description + "</td>"
			+ "<td class=\"column3\">Salle " + json[i].localisation + "</td>"
			+"<td class=\"column4\"><a onclick=\"session.raiseEvent('go_to_room/Room"+ json[i].localisation + "', true);\" href=\"#\" class=\"button\">Go &#x25B6;</a></td>"
			+ "</tr>";
		}
	},
	error: function(error) {
		showError(JSON.stringify(error))
	}
})