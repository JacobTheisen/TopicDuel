import { BabelFileResult } from "@babel/core";

type IframProps = {
  code: undefined | BabelFileResult;
};

function iframe(props: IframProps) {
  const source = /* html */ `
    <html>
    <body>
      <div id="app"></div>
      <script type="module">${props.code ? props.code.code : ""}</script>
    </body>
    </html>
  `;

  return <iframe title={"output"} srcDoc={source} data-iframe></iframe>;
}

export default iframe;
