function CheckAnswers() {
    let Q1Answer = document.querySelector("input[name='Q1']:checked")
    let Q2Answer = document.querySelector("input[name='Q2']:checked")
    let Q3Answer = document.querySelector("input[name='Q3']:checked")
    let Q4Answer = document.querySelector("input[name='Q4']:checked")
    let Q5Answer = document.querySelector("input[name='Q5']:checked")

    let result = document.getElementById("result")

    if (Q1Answer && Q2Answer && Q3Answer && Q4Answer && Q5Answer)
    {
        let score = 0;
        if (Q1Answer.value === "b")
        {
            score++
        }

        if (Q2Answer.value === "a")
        {
            score++
        }

        if (Q3Answer.value === "b")
        {
            score++
        }

        if (Q4Answer.value === "c")
        {
            score++
        }

        if (Q5Answer.value === "a")
        {
            score++
        }

        result.innerHTML = `The score is ${score} / 5`
    }
}