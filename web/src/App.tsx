import reactLogo from "./assets/react.svg";
import InitCsv from "./components/init";
import Wrapper from "./components/wrapper";
import StyleProvider from "./style";

function App() {
  return (
    <StyleProvider>
      <Wrapper>
        <span>Test</span>
      </Wrapper>
    </StyleProvider>
  );
}

export default App;
