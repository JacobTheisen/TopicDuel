type EditorProps = {
  setCode: (a: any) => void;
};

function Editor(props: EditorProps) {
  return (
    <textarea
      spellCheck="false"
      data-editor
      onChange={(e) => props.setCode(e.target.value)}
    ></textarea>
  );
}

export default Editor;
