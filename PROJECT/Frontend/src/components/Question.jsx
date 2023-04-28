import { useState } from "react";

export default function Question({
  question = {},
  setCurrentQuestionIndex,
  setCorrectAnsCounter,
  isLastQuestion,
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
          <li
            className={`${selectedAns === option ? "selected" : ""}`}
            onClick={() => handleSelectOption(option)}
            key={index}
          >
            {option}
          </li>
        ))}
      </ul>
      {!isLastQuestion && <button onClick={handleNextBtn}>Next</button>}
    </section>
  );
}

Question.propTypes = {
  question: () => {},
  setCurrentQuestionIndex: () => {},
  setCorrectAnsCounter: () => {},
  isLastQuestion: () => Boolean(),
};
