import Editor from "../components/EditorIn";
import Iframe from "../components/IframOut";
import { Button } from "@mui/material";
import { transform } from "@babel/standalone";
import { BabelFileResult } from "@babel/core";
import { useState } from "react";

function Main() {
  const [code, setCode] = useState<string>("");
  const [transpiledCode, setTranspildeCode] = useState<BabelFileResult>();

  function transpileCode() {
    const options = { presets: ["es2015-loose", "react"] };
    if (code) {
      let tCode = transform(code, options);
      if (tCode) {
        setTranspildeCode(tCode);
        console.log(tCode);
      }
    }
  }
  return (
    <>
      <section>
        <Iframe code={transpiledCode}></Iframe>
      </section>
      <section>
        <Editor setCode={setCode}></Editor>
      </section>
      <Button
        onClick={() => transpileCode()}
        sx={{ boxShadow: 5, backgroundColor: "lightblue", color: "white" }}
      >
        Click me
      </Button>
    </>
  );
}

export default Main;
