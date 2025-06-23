$(document).ready(function () {

	function readURL(input) {
		if (input.files && input.files[0]) {
			var reader = new FileReader();

			reader.onload = function (e) {
				$('#selected_image')
					.attr('src', e.target.result)
					.width(176)
					.height(176);
			}
			reader.readAsDataURL(input.files[0]);
		}
	}

	$('#imagefile').change(function () {
		readURL(this);
	});

	$('#cameraInput').change(function () {
		readURL(this);
	
		// Copy the captured file to #imagefile so the existing analysis code works
		const capturedFile = this.files[0];
		if (capturedFile) {
			// create a new FileList for #imagefile
			const dataTransfer = new DataTransfer();
			dataTransfer.items.add(capturedFile);
			document.getElementById('imagefile').files = dataTransfer.files;
		}
	});


	$("form#analysis-form").submit(function (event) {
		event.preventDefault();

		var analyze_button = $("button#analyze-button");
		var imagefile = $('#imagefile')[0].files;

		if (!imagefile.length > 0) {
			alert("Please select a file to analyze!");
		}
		else {
			analyze_button.html("Analyzing..");
			analyze_button.prop("disabled", "true");

			$("#output").html("");
    		$("#overview").html("");
    		$("#remedy").html("");

			var fd = new FormData();
			fd.append('file', imagefile[0]);

			var loc = window.location;

			$.ajax({
				method: 'POST',
				async: true,
				url: loc.protocol + '//' + loc.hostname + ':' + loc.port + '/analyze',
				data: fd,
				processData: false,
				contentType: false,
			}).done(function (data) {
				console.log("Done Request!");
				$("#output").html(data.disease_name);
				$.ajax({
					method: 'POST',
					url: loc.protocol + '//' + loc.hostname + ':' + loc.port + '/get-remedy', 
					contentType: 'application/json',
					data: JSON.stringify({ disease_name: data.disease_name }),
				})
				.done(function (remedyData) {
					
					$("#overview").append("<br><br><strong>Overview:</strong> " + remedyData.overview);
					$("#remedy").append("<br><strong>Remedies:</strong> " + remedyData.remedy);
				})
				.fail(function (err) {
					console.log("Failed to fetch remedy.");
					$("#output-text").append("<br><br>Could not fetch remedy information.");
				});
			}).fail(function (e) {
				console.log("Fail Request!");
				console.log(e);
				$("#output").html("Failed to analyze image.");
    			analyze_button.prop("disabled", "");
    			analyze_button.html("Analyze");
			});
		};

		analyze_button.prop("disabled", "");
		analyze_button.html("Analyze");
		console.log("Submitted!");
	});
});


