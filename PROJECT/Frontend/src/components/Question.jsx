// eslint-disable-next-line react/prop-types
export default function Question({ question = {} }) {
  return (
    <section>
      <p>{question.question}</p>
      <ul>
        {question.options?.map((option, index) => (
          <li key={index}>{option}</li>
        ))}
      </ul>
    </section>
  );
}
