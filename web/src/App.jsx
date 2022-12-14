import { StyleProvider } from "./styles";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Main from "./components/main";

const App = () => {
  return (
    <StyleProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Main />} />
        </Routes>
      </BrowserRouter>
    </StyleProvider>
  );
};

export default App;
