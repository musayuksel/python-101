import { useState } from "react";

// eslint-disable-next-line react/prop-types
export default function Question({
  question = {},
  setCurrentQuestionIndex,
  setCorrectAnsCounter,
}) {
  const [selectedAns, setSelectedAns] = useState("");

  console.log({ ANSWER: question.answer });
  function handleSelectOption(option) {
    setSelectedAns(option);
  }

  function handleNextBtn() {
    if (selectedAns === question.answer) {
      setCorrectAnsCounter((prev) => prev + 1);
    }
    setCurrentQuestionIndex((prev) => prev + 1);
  }

  return (
    <section>
      <p>{question.question}</p>
      <ul className="question-options-container">
        {question.options?.map((option, index) => (
          <li onClick={() => handleSelectOption(option)} key={index}>
            {option}
          </li>
        ))}
      </ul>
      <button onClick={handleNextBtn}>Next</button>
    </section>
  );
}
