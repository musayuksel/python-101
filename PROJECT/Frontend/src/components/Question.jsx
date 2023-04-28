export default function Question({ question }) {
  const { question: questionText, options, answer } = question;
  return (
    <section>
      <p>{questionText}</p>
      <ul>
        {options?.map((option, index) => (
          <li key={index}>{option}</li>
        ))}
      </ul>
    </section>
  );
}
