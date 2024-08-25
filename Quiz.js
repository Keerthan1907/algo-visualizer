function checkAnswer() {
    const answer1 = document.getElementById('answer1').value;
    const resultDiv = document.getElementById('result');
    if (answer1.toLowerCase() === 'correct answer') {
        resultDiv.innerHTML = '<p>Correct!</p>';
    } else {
        resultDiv.innerHTML = '<p>Try again.</p>';
    }
}
