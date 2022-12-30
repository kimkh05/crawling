import reactLogo from "./assets/react.svg";
import InitCsv from "./components/init";
import StyleProvider from "./style";
import { QueryClient, QueryClientProvider } from "react-query";

const App = () => {
  const queryClient: QueryClient = new QueryClient();
  return (
    <StyleProvider>
      <QueryClientProvider client={queryClient}>
        <span>Test</span>
      </QueryClientProvider>
    </StyleProvider>
  );
}

export default App;
